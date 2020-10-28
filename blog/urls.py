from django.urls import path

from .views import Homepage, PostView, PostsByCategory

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("<str:slug>", PostView.as_view(), name="post"),
    path("category/<str:slug>/", PostsByCategory.as_view(), name="category_page"),
]
