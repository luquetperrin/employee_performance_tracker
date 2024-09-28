from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Service, User

class ServiceTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        self.service = Service.objects.create(name='Test Service', manager=self.user)

    def test_create_service(self):
        url = reverse('service-list')
        self.client.login(username='testuser', password='password123')
        data = {'name': 'New Service', 'manager': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_services(self):
        url = reverse('service-list')
        self.client.login(username='testuser', password='password123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
