from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User

class UserLoginTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')

    def test_login_success(self):
        url = reverse('user-login')
        data = {
            'username': 'testuser',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_invalid_credentials(self):
        url = reverse('user-login')
        data = {
            'username': 'wronguser',
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
