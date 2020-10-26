from django.urls import path

from .views import Homepage, PostView

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("<str:slug>", PostView.as_view(), name="post"),
]
