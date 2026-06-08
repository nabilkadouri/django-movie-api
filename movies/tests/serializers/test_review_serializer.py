from django.test import TestCase
from movies.models import Movie,Review
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
            duration= 180,
            image="https://image.png",
        )
        
        self.factory = APIRequestFactory()
        
        self.request = self.factory.post("/reviews/")
        self.request.user = self.user
        
    # Test Review
    def test_review_valid(self):
        
        data = {
            "movie": self.movie.id,
            "rating" : 5,
            "comment" : "Super film",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()

        self.assertTrue(is_valid)


    # Tests Rating
    def test_rating_cannot_be_zero(self):
        
        data = {
            "movie": self.movie.id,
            "rating" : 0,
            "comment" : "Super film",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn("rating", serializer.errors)
        self.assertEqual(
            serializer.errors["rating"][0],
            "La note doit être comprise entre 1 et 10."
        )
        
    def test_rating_cannot_be_greater_than_ten(self):
        
        data = {
            "movie": self.movie.id,
            "rating" : 11,
            "comment" : "Super film",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn("rating", serializer.errors)
        self.assertEqual(
            serializer.errors["rating"][0],
            "La note doit être comprise entre 1 et 10."
        )
        
    def test_rating_minimum_valid(self):
        
        data = {
            "movie": self.movie.id,
            "rating" : 1,
            "comment" : "Super film",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
    def test_rating_maximum_valid(self):
        
        data = {
            "movie": self.movie.id,
            "rating" : 10,
            "comment" : "Super film",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
    # Tests comment
    def test_comment_trim_spaces(self):
           
        data = {
            "movie": self.movie.id,
            "rating" : 1,
            "comment" : " Super film ",
            }
        
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        self.assertEqual(
            serializer.validated_data["comment"],
            "Super film"
        )
        
    def test_comment_can_be_blank(self):
        
        data = {
            "movie": self.movie.id,
            "rating" : 1,
            "comment" : "",
        }
    
        serializer = ReviewSerializer(
            data=data,
            context={"request": self.request}
            )
    
        is_valid = serializer.is_valid()
        print(is_valid)
        self.assertTrue(is_valid)

    # Test 
    def test_user_cannot_review_same_movie_twice(self):
        
        Review.objects.create(
            user=self.user,
            movie=self.movie,
            rating=5,
            comment="Test 1er avis"
        )
        
        data = {
            "movie": self.movie.id,
            "rating" : 8,
            "comment" : " Test 2éme avis ",
            }
        
        serializer = ReviewSerializer(
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
            "Le film sélectionné ne doit pas être noté plusieurs fois."
        )
        
        
        