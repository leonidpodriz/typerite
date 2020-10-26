from django.views.generic import ListView, DetailView
from .models import Post


class Homepage(ListView):
    template_name = "blog/homepage.html"
    queryset = Post.objects.all()


class PostView(DetailView):
    template_name = 'blog/single.html'
    queryset = Post.objects.all()
