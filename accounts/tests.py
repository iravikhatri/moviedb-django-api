from rest_framework.test import APITestCase
from .models import User


class TestUser(APITestCase):

    url = '/api/users/'

    def setUp(self):
        data = {
            'first_name': 'Jake',
            'last_name': 'gyllenhaal',
            'username': 'jakegyllenhaal',
            'email': 'jake@gyllenhaal.com',
            'password': 'qwerty@123',
            'is_admin': False,
        }
        User.objects.create_user(**data)

    def test_get_user(self):
        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['username'], 'jakegyllenhaal')

    def test_post_user(self):
        # data
        data = {
            'username': 'joaquinphoenix',
            'email': 'joaquin@phoenix.com',
            'password': 'qwerty@789',
            'is_admin': True,
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['username'], 'joaquinphoenix')

    def test_update_user(self):
        # data
        pk = "1"
        data = {
            'last_name': 'Gyllenhaal',
        }

        # process
        self.client.login(username='jakegyllenhaal', password='qwerty@123')
        response = self.client.patch(f'{self.url}{pk}/', data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['last_name'], data['last_name'])

    def test_delete_user(self):
        pk = "1"

        # process
        self.client.login(username='jakegyllenhaal', password='qwerty@123')
        response = self.client.delete(f'{self.url}{pk}/')

        # assert
        self.assertEqual(response.status_code, 204)
