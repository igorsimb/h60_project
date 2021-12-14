from django.urls import path
from .views import IndexView, DeleteMovieView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('movie/<int:pk>/delete/', DeleteMovieView.as_view(), name='delete-movie'),
]