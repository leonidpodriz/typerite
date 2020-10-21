from django.contrib.auth import get_user_model
from django.db import models

from core.models import UnregisteredUser

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)


class Tag(models.Model):
    name = models.CharField(max_length=10)


class Post(models.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    title = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    datetime = models.DateTimeField(auto_now_add=True)
    datetime_edit = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=20)


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    message = models.TextField()
    commentator = models.ForeignKey(UnregisteredUser, on_delete=models.CASCADE)
