from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import PostForm, CommentForm
from .models import Post, Comment


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish')
    template_name = 'blog/post_list.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.get_object()).order_by('-created_on')
        return context

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
        else:
            context = self.get_context_data(form=form)
            context['comment_form'] = form
            return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    login_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Post updated successfully.")
        return response

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy('blog:post_detail', kwargs={'pk': post.pk})

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_superuser or self.request.user == post.author:
            return True
        else:
            messages.error(self.request, "You do not have permission to edit this post.")
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    login_url = '/login/'

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_superuser or self.request.user == post.author:
            return True
        else:
            messages.error(self.request, "You do not have permission to delete this post.")
            return False
