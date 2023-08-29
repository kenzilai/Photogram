from django.urls import path
from .views import HomePageView, PhotoDetailView, NewPhoto

app_name = 'gallery'

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("album/<int:pk>/", PhotoDetailView.as_view(), name="album"),
    path("album/new", NewPhoto.as_view(), name="new")
]