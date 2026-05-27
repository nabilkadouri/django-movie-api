from django.urls import path
from .views.movie_views import MovieView, MovieDetailView
from .views.category_views import CategoryView
from .views.director_views import DirectorView, DirectorDetailView
from .views.actor_views import ActorView, ActorDetailView
from .views.favorite_views import FavoriteView
from .views.review_views import ReviewView,ReviewDetailView

urlpatterns = [
    path("", MovieView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),

    path("categories/", CategoryView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryView.as_view(), name="category-detail"),

    path("directors/", DirectorView.as_view(), name="director-list"),
    path("directors/<int:pk>/", DirectorDetailView.as_view(), name="director-detail"),

    path("actors/", ActorView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),

    path("favorites/", FavoriteView.as_view(), name="favorite-list"),
    path("favorites/<int:pk>/", FavoriteView.as_view(), name="favorite-detail"),

    path("reviews/", ReviewView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]