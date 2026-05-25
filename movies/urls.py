from django.urls import path
from .views.movie_views import MovieView
from .views.category_views import CategoryView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("categories/", CategoryView.as_view()),
    
]