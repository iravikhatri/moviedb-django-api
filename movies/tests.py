from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from .models import Movie


class TestUser(APITestCase):

    url = '/api/movies/'

    def setUp(self):
        user_data = {
            'username': 'jakegyllenhaal',
            'email': 'jake@gyllenhaal.com',
            'password': 'qwerty@123',
            'is_admin': True,
        }
        get_user_model().objects.create_user(**user_data)
        self.client.login(username='jakegyllenhaal', password='qwerty@123')

        movie_data = {
            "name": "Terminator 2 : Judgment Day",
            "director": "James Cameron",
            "popularity": 85.0,
            "imdb_score": 8.5,
        }

        Movie.objects.create(**movie_data)

    def test_get_movie(self):
        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], 'Terminator 2 : Judgment Day')

    def test_post_movie(self):
        # data
        data = {
            "name": "A Nightmare on Elm Street",
            "director": "Wes Craven",
            "imdb_score": 7.4,
            "popularity": 74.0,
            "genre": [
                "Horror",
                " Mystery"
            ]
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['name'], 'A Nightmare on Elm Street')

    def test_update_movie(self):
        # data
        pk = "1"
        data = {
            'popularity': 89,
        }

        # process
        response = self.client.patch(f'{self.url}{pk}/', data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['popularity'], data['popularity'])

    def test_delete_movie(self):
        pk = "1"

        # process
        response = self.client.delete(f'{self.url}{pk}/')

        # assert
        self.assertEqual(response.status_code, 204)
