
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"