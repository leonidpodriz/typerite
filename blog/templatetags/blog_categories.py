from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag(
    "blog/tags/categories.html",
    name="categories"
)
def get_categories():
    return {
        "categories": Category.objects.all()
    }
