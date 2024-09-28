from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User

class UserAuthTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')

    def test_auth_required_for_profile_view(self):
        url = reverse('user-profile', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required_for_profile_update(self):
        url = reverse('user-profile', args=[self.user.id])
        data = {'email': 'newemail@example.com'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
