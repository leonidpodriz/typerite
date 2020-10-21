from django.db import models


class UnregisteredUser(models.Model):
    name = models.CharField(max_length=20)
    web_site = models.URLField(max_length=255)
    email = models.EmailField()
    ip = models.GenericIPAddressField(blank=True, null=True)


class ContactMessage(models.Model):
    message = models.TextField()
    author = models.ForeignKey(UnregisteredUser, on_delete=models.CASCADE)


class Social(models.Model):
    name = models.CharField(max_length=20)
    icon_name = models.CharField(max_length=20)
    link = models.URLField(max_length=255)
