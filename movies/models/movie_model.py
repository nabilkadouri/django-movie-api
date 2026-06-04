from django.db import models
from django.contrib.auth import get_user_model
from .category_model import Category
from .director_model import Director
from .actor_model import Actor

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    duration = models.IntegerField()
    image = models.URLField()
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
        blank=True
    )
    
    
    categories = models.ManyToManyField(
        Category,
        related_name="movies",
        blank=True
        )
    
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
        blank=True
        )
    
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
        null=True,
        blank=True
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title