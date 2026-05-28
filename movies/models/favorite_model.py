from django.db import models
from django.contrib.auth import get_user_model
from .movie_model import Movie

User= get_user_model()
class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
        )
    
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="favorites"
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} - {self.movie.title}"