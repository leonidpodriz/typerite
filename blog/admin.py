from django.contrib import admin

from .models import Post, Comment, Category, Tag


class CommentTabularInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "datetime", "datetime_edit", "author", "slug")
    inlines = [CommentTabularInline]
