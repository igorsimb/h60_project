from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView
from django.contrib.auth import get_user_model

from .models import Movie
from .forms import CreateMovieForm

User = get_user_model()


class IndexView(CreateView):
    form_class = CreateMovieForm
    template_name = 'base/index.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context


class DeleteMovieView(DeleteView):
    model = Movie
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)