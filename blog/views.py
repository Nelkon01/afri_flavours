from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-created_on')

    template_name = 'blog/post_list.html'
    paginate_by = 5


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
