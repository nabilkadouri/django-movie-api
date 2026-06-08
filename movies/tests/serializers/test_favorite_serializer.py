from django.test import TestCase
from django.contrib.auth import get_user_model
from movies.serializers.favorite_serializer import FavoriteSerializer
from rest_framework.test import APIRequestFactory
from movies.models import Favorite, Movie

User = get_user_model()

class FavoriteSerializerTest(TestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(
            username="nabil",
            password="password123"
        )
        
        self.movie = Movie.objects.create(
            title="Gladiator",
            description="Film fr",
            release_year=1999,
            duration= 180,
            image="https://image.png",
        )
        
        self.factory = APIRequestFactory()
        
        self.request = self.factory.post("/favorites/")
        self.request.user = self.user
        
    def test_favorite_valid(self):
        
        data = {
            "movie": self.movie.id
        }
        
        serializer = FavoriteSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
        
    def test_user_cannot_favorite_same_movie_twice(self):
        
        Favorite.objects.create(
            user=self.user,
            movie=self.movie,
        )
        
        data = {
            "movie": self.movie.id
        }
        
        serializer = FavoriteSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        
        self.assertIn(
            "non_field_errors",
            serializer.errors
        )

        self.assertEqual(
            serializer.errors["non_field_errors"][0],
            "Le film sélectionné a déjà été mis en favori."
        )
        