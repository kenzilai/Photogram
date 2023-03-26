from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photo


class HomePageView(TemplateView):
    http_method_names = ["get"]
    template_name = "gallery/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photo.objects.all().order_by("-id")[0:30]
        return context
    
class PhotoDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "gallery/album.html"
    model = Photo
    context_object_name = "photo"

class NewPhoto(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = "gallery/new.html"
    fields = ["title", "image", "description"]