from django.test import TestCase
from movies.models import Movie
from django.contrib.auth import get_user_model
from movies.serializers.review_serializer import ReviewSerializer
from rest_framework.test import APIRequestFactory

User = get_user_model()

class ReviewSerializerTest(TestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(
            username="nabil",
            password="password123"
        )
        
        self.movie = Movie.objects.create(
            title="Gladiator",
            description="Film fr",
            release_year=1999,
            duration="180",
            image="https://image.png",
        )
        
    
    def test_review_valid(self):
        factory = APIRequestFactory()
        request = factory.post("/reviews/")
        request.user = self.user
        data = {
            "user" : self.user.id,
            "movie": self.movie.id,
            "rating" : 5,
            "comment" : "Super film",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": request}
            )
        
        is_valid = serializer.is_valid()

        print(is_valid)
        print(serializer.errors)

        self.assertTrue(is_valid)
