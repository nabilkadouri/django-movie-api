from django.db import models

from django.contrib.auth import get_user_model

from .movie_model import Movie


User =get_user_model()

class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.IntegerField()

    comment = models.TextField(
        blank=True,
        default=""
        )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"