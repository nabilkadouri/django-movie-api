from django.contrib import admin

from .models import (
    Movie,
    Review,
    Favorite,
    Actor,
    Director,
    Category
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "release_year",
        "is_published",
        "created_by",
        "created_at",
    )

    list_filter = (
        "is_published",
        "release_year",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "movie",
        "user",
        "rating",
        "comment",
    )

    list_filter = (
        "rating",
    )

    search_fields = (
        "movie__title",
        "user__username",
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "movie",
    )

    search_fields = (
        "user__username",
        "movie__title",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "first_name",
        "last_name",
    )

    search_fields = (
        "first_name",
        "last_name",
    )


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "first_name",
        "last_name",
    )

    search_fields = (
        "first_name",
        "last_name",
    )