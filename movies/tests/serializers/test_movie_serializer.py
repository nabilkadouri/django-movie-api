from django.test import TestCase
from movies.serializers import MovieSerializer
from movies.models import Movie
from django.utils import timezone


class MovieSerializerTest(TestCase):
    
    # Test Movie
    def test_movie_valid(self):
        
        data = {
            "title" : "Armagedon",
            "description": "Super film.",
            "release_year": 1998,
            "duration": 151,
            "image": "https://upload.wikimedia.org/wikipedia/en/f/f9/Armageddonposter.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
        
    # Tests Title
    def test_title_blank(self):
        
        data = {
            "title" : "",
            "description": "Super film.",
            "release_year": 1998,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)

        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn("title", serializer.errors)
        
    def test_title_too_short(self):
        
        data = {
            "title" : "ab",
            "description": "Super film.",
            "release_year": 1998,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn(
            "title",
            serializer.errors
        )
        self.assertEqual(
            serializer.errors["title"][0],
            "Le titre doit contenir au moins 3 caractères."
        )
        
    def test_title_minimum_length(self):
        
        data = {
            "title" : "abc",
            "description": "Super film.",
            "release_year": 1998,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
    def test_title_duplicate(self):

        Movie.objects.create(
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png"
        )

        data = {
            "title": "armageddon",
            "description": "Autre film",
            "release_year": 1998,
            "duration": 151,
            "image": "https://image.png"
        }

        serializer = MovieSerializer(data=data)

        is_valid = serializer.is_valid()

        self.assertFalse(is_valid)

        self.assertIn(
            "title",
            serializer.errors
        )

        self.assertEqual(
            serializer.errors["title"][0],
            "Ce film existe déjà."
        )
        
    def test_title_capitalize(self):

        data = {
            "title": "gLaDiaTor",
            "description": "Super film.",
            "release_year": 1998,
            "duration": 151,
            "image": "https://test.jpg",
        }

        serializer = MovieSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        self.assertEqual(
            serializer.validated_data["title"],
            "Gladiator"
        )
        
       
    # Tests Description
    def test_description_trim_spaces(self):
        
        data = {
            "title" : "Armageddon",
            "description": "  Super film. ",
            "release_year": 1998,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)

        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        self.assertEqual(
            serializer.validated_data["description"],
            "Super film."
        )
        
    
    # Tests Release_year
    def test_release_year_cannot_be_in_future(self):
         
        data = {
            "title" : "Armageddon",
            "description": "Super film.",
            "release_year": 2027,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        
        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn("release_year", serializer.errors)
        self.assertEqual(
            serializer.errors["release_year"][0],
            "L'année de réalisation du film ne doit pas être dans le futur."
        )
        
    def test_release_year_cannot_be_before_1888(self):
        
        data = {
            "title" : "Armageddon",
            "description": "Super film.",
            "release_year": 1880,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        
        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn("release_year", serializer.errors)
        self.assertEqual(
            serializer.errors["release_year"][0],
            "L'année du film est trop ancienne."
        )
        
    def test_release_year_minimum_valid(self):
        
        data = {
            "title" : "Armageddon",
            "description": "Super film.",
            "release_year": 1888,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
    def test_release_year_current_year_valid(self):
        
        current_year = timezone.now().year
        
        data = {
            "title" : "Armageddon",
            "description": "Super film.",
            "release_year": current_year,
            "duration": 151,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)
        
        is_valid = serializer.is_valid()
        
        self.assertTrue(is_valid)
        
        
    # Tests Duration
    def test_duration_too_short(self):
        
        data = {
            "title" : "Armageddon",
            "description": "  Super film. ",
            "release_year": 1998,
            "duration": 39,
            "image": "https://test.jpg",
        }
        
        serializer = MovieSerializer(data=data)

        is_valid = serializer.is_valid()
        
        self.assertFalse(is_valid)
        self.assertIn("duration", serializer.errors)
        self.assertEqual(
            serializer.errors["duration"][0],
            "Un film doit durer au moins 40 minutes."
        )
              
    def test_duration_minimum_valid(self):

        data = {
            "title": "Armageddon",
            "description": "Super film.",
            "release_year": 1998,
            "duration": 40,
            "image": "https://test.jpg",
        }

        serializer = MovieSerializer(data=data)

        is_valid = serializer.is_valid()

        self.assertTrue(is_valid)