from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category


class Homepage(ListView):
    template_name = "blog/homepage.html"
    queryset = Post.objects.all()


class PostView(DetailView):
    template_name = 'blog/single.html'
    queryset = Post.objects.all()


class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset.filter(categories__slug__contains=self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        context.update({"category_name": category.name})

        return context
