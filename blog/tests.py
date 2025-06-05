from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post, Comment


class BlogModelTests(TestCase):
    def test_post_and_comment_str(self):
        user = User.objects.create(username="author")
        post = Post.objects.create(title="Title", author=user, body="Body", status=Post.Status.PUBLISHED)
        comment = Comment.objects.create(author="Anon", body="hi", post=post)
        self.assertEqual(str(post), "Title")
        self.assertIn("Anon", str(comment))


class BlogViewsTests(TestCase):
    def setUp(self):
        user = User.objects.create(username="author")
        self.post = Post.objects.create(title="A", author=user, body="b", status=Post.Status.PUBLISHED)

    def test_post_list_view(self):
        url = reverse("blog:post_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertIn(self.post, response.context["posts"])

    def test_post_detail_view(self):
        url = reverse("blog:post_detail", args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
        self.assertEqual(response.context["object"], self.post)
