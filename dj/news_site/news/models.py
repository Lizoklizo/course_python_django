# news/models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name = models.CharField(max_length=255)

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
