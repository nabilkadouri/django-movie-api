from django.db import models
from .category_model import Category
from .director_model import Director
from .actor_model import Actor

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    duration = models.IntegerField()
    image = models.URLField()
    is_published = models.BooleanField(default=True)
    
    
    categories = models.ManyToManyField(Category, related_name="movies")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title