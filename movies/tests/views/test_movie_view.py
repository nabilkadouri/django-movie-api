from rest_framework.test import APITestCase
from movies.models import Movie
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieViewTest(APITestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(
            username="nabil",
            password="password123"
        )
        
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="password123"
        )
        
        self.other_user = User.objects.create_user(
        username="john",
        password="password123"
        )
        
        
    # GET/movies/
    def test_get_movies_returns_empty_list(self):
        
        url = reverse("movie-list") 
        
        response = self.client.get(url)
        
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response.data,
            []
        )
        
    def test_get_movies_returns_movies(self):
        
        Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png"
        )
        
        Movie.objects.create (
            title="Gladiator",
            description="Film",
            release_year=2000,
            duration=155,
            image="https://image.png"
        )
        
        url = reverse("movie-list") 
        
        response = self.client.get(url)
        
        self.assertEqual(
            response.status_code,
            200
        )
        
        self.assertEqual(
            len(response.data),
            2
        )
        
        
    # POST/movies/
    def test_anonymous_user_cannot_create_movie(self):
        
        url = reverse("movie-list")
        
        data = {
            "title": "armageddon",
            "description": "Film",
            "release_year": 1998,
            "duration": 151,
            "image": "https://image.png"
        }
        
        response = self.client.post(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            401
        )
        
    def test_authenticated_user_can_create_movie(self):
        
        self.client.force_authenticate(
            user=self.user
        )
        
        url = reverse("movie-list")
        
        data = {
            "title": "armageddon",
            "description": "Film",
            "release_year": 1998,
            "duration": 151,
            "image": "https://image.png"
        }
        
        response = self.client.post(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            201
        )
        
        self.assertEqual(
            Movie.objects.count(),
            1
        )
        
    def test_create_movie_with_invalid_data_returns_400(self):
        
        self.client.force_authenticate(
            user=self.user
        )
        
        url = reverse("movie-list")
        
        data = {
            "title": "",
            "description": "Film",
            "release_year": 1998,
            "duration": 151,
            "image": "https://image.png"
        }
        
        response = self.client.post(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            400
        )
        
        
    # GET/movies/<id>/
    def test_get_movie_detail_returns_200(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png"
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        response = self.client.get(url)
        
        self.assertEqual(
            response.status_code,
            200
        )
        
    def test_get_movie_detail_returns_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png"
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        response = self.client.get(url)
        
        self.assertEqual(
            response.data["title"],
            "Armageddon"
        )
    
    def test_get_movie_detail_returns_404(self):
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":999}
        )
        
        response = self.client.get(url)
        
        self.assertEqual(
            response.status_code,
            404
        )
        
    # PATCH/movies/<id>/
    def test_owner_can_patch_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        self.client.force_authenticate(
            user=self.user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        data = {
            "description": "Super film",
            "image": "https://patchImage.png"
        }
        
        response = self.client.patch(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            200
        )
        
        movie.refresh_from_db()
        
        self.assertEqual(
            movie.description,
            "Super film"
        )
        
        self.assertEqual(
            movie.image,
            "https://patchImage.png"
        )

    def test_admin_can_patch_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        self.client.force_authenticate(
            user=self.admin
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        data = {
            "description": "Super film",
            "image": "https://patchImage.png"
        }
        
        
        response = self.client.patch(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            200
        )
        
        movie.refresh_from_db()
        
        self.assertEqual(
            movie.description,
            "Super film"
        )
        self.assertEqual(
            movie.image,
            "https://patchImage.png"
        )

    def test_anonymous_user_cannot_patch_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        data = {
            "description": "Super film",
            "image": "https://patchImage.png"
        }
        
        
        response = self.client.patch(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            401
        )
        
    def test_non_owner_cannot_patch_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        self.client.force_authenticate(
            user=self.other_user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        data = {
            "description": "Super film",
            "image": "https://patchImage.png"
        }
        
        
        response = self.client.patch(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            403
        )
    
    def test_patch_movie_with_invalid_image_returns_400(self):

        movie = Movie.objects.create(
            title="Titanic",
            description="Super Film",
            release_year=1998,
            duration=165,
            image="https://film.png",
            created_by=self.user
        )

        self.client.force_authenticate(
            user=self.user
        )

        url = reverse(
            "movie-detail",
            kwargs={"pk": movie.id}
        )

        data = {
            "image": ""
        }

        response = self.client.patch(
            url,
            data,
            format="json"
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            400
        )
        
        
    # PUT/movies/<id>/
    def test_owner_can_put_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        self.client.force_authenticate(
            user=self.user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        data = {
            "title": "Armageddon",
            "description": "Super film",
            "release_year": 1998,
            "duration": 151,
            "image": "https://image.png"
        }
        
        response = self.client.put(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            200
        )
        
        movie.refresh_from_db()
        
        self.assertEqual(
            movie.description,
            "Super film"
        )

    def test_non_owner_cannot_put_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )

        self.client.force_authenticate(
            user=self.other_user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )

        data = {
            "title": "Armageddon",
            "description": "Super film",
            "release_year": 1998,
            "duration": 151,
            "image": "https://image.png"
        }
        
        response = self.client.put(
            url,
            data,
            format="json"
        )
        
        self.assertEqual(
            response.status_code,
            403
        )
    
    # DELETE/movies/<id>
    def test_owner_can_delete_movie(self):
        
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        self.client.force_authenticate(
            user=self.user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        
        response = self.client.delete(
            url
        )
        
        self.assertEqual(
            response.status_code,
            204
        )
        
        self.assertFalse(
            Movie.objects.filter(
                pk=movie.id
            ).exists()
        )
        
    def test_non_owner_cannot_delete_movie(self):
    
        movie = Movie.objects.create (
            title="Armageddon",
            description="Film",
            release_year=1998,
            duration=151,
            image="https://image.png",
            created_by=self.user
        )
        
        self.client.force_authenticate(
            user=self.other_user
        )
        
        url = reverse(
            "movie-detail",
            kwargs={"pk":movie.id}
        )
        
        response = self.client.delete(
            url
        )
        
        self.assertEqual(
            response.status_code,
            403
        )
        
        self.assertTrue(
        Movie.objects.filter(
            pk=movie.id
        ).exists()
        )
        