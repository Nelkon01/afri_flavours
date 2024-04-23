from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    class Status:
        DRAFT = 'draft'
        PUBLISHED = 'published'
        CHOICES = (
            (DRAFT, 'Draft'),
            (PUBLISHED, 'Published'),
        )

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.CHOICES, default=Status.DRAFT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
