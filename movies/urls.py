from django.urls import path
from .views.movie_views import MovieView, MovieDetailView
from .views.category_views import CategoryView

urlpatterns = [
    path("movies/", MovieView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("categories/", CategoryView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryView.as_view(), name="category-detail")
]