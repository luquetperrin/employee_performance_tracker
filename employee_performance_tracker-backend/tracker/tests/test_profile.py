from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User

class UserProfileTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')

    def test_view_user_profile(self):
        url = reverse('user-profile', args=[self.user.id])
        self.client.login(username='testuser', password='password123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_profile(self):
        url = reverse('user-profile', args=[self.user.id])
        self.client.login(username='testuser', password='password123')
        data = {'email': 'newemail@example.com'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
