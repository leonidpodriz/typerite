from django.db import models


class UnregisteredUser(models.Model):
    name = models.CharField(max_length=20)
    web_site = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    message = models.TextField()
    author = models.ForeignKey(UnregisteredUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message from {self.author}"


class Social(models.Model):
    SOCIALS = (
        ("ss-facebook", "Facebook"),
        ("ss-twitter", "Twitter"),
        ("ss-dribble", "Dribble"),
        ("ss-behance", "Behance"),
        ("ss-instagram", "Instagram"),
        ("ss-pinterest", "Pinterest"),
        ("ss-rss", "RSS"),
    )

    name = models.CharField(max_length=20)
    icon_name = models.CharField(max_length=20, choices=SOCIALS, default="ss-facebook")
    link = models.URLField(max_length=255)
    is_visible = models.BooleanField(verbose_name="Visible")

    def __str__(self):
        return self.name
