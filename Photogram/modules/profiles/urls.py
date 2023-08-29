from django.urls import path
from .views import ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path("profile/<str:username>/", ProfileDetailView.as_view(), name="detail"),
]