from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


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


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
