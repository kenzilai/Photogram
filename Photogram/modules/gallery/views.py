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
    template_name = "gallery/new.html"
    model = Photo
    success_url = "/"
    fields = ["title", "image", "description"]

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        
        def dispatch(self, request, *args, **kwargs):
            self.request = request
            return super().dispatch(request, *args, **kwargs)
        
        
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)