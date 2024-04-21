from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish')
    template_name = 'blog/post_list.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the user is a superuser
        context['is_superuser'] = self.request.user.is_superuser
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk=comment.post.pk)
        else:
            context = self.get_context_data(form=form)
            context['comment_form'] = form
            return self.render_to_response(context)


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
