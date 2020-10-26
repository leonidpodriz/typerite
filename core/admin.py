from django.contrib import admin

from .models import UnregisteredUser, ContactMessage, Social


@admin.register(UnregisteredUser)
class UnregisteredUserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "web_site", "ip")
    list_display_links = ("name",)
    list_filter = ("ip",)
    list_editable = ("email", "web_site")
    search_fields = ("name", "email", "web_site", "ip")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("author",)
    list_filter = ("author",)
    search_fields = ("author", "message")


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("name", "icon_name", "link", "is_visible")
    list_display_links = ("name", "icon_name")
    list_filter = ("name", "icon_name", "is_visible")
    search_fields = ("name", "link")
    list_editable = ("is_visible",)
