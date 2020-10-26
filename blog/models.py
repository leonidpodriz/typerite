from django.contrib.auth import get_user_model
from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify

from core.models import UnregisteredUser

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    title = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    datetime = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)
    datetime_edit = models.DateTimeField(verbose_name="Last edit date", auto_now=True)
    content = QuillField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=20, default="", editable=False)

    @classmethod
    def _get_slug(cls, title):
        title_slug = slugify(title)
        count_with_same_slug = cls.objects.filter(slug=title_slug).count()

        if count_with_same_slug is not 0:
            return f"{title_slug}-{count_with_same_slug}"

        return title_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    message = models.TextField()
    commentator = models.ForeignKey(UnregisteredUser, on_delete=models.CASCADE)
