from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User  # Import your User model if needed

class UserRegistrationTest(APITestCase):

    def test_user_registration(self):
        url = reverse('user-registration')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'role': 'employee',  # Use a valid role
        }
        response = self.client.post(url, data, format='json')
        
        # Check that the response was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check that 'username' is in the nested 'data' key in response
        self.assertEqual(response.data['data']['username'], data['username'])  # Check the username

    def test_user_registration_with_existing_username(self):
        url = reverse('user-registration')
        
        # Register the first user
        self.client.post(url, {
            'username': 'existinguser',
            'email': 'existinguser@example.com',
            'password': 'password123',
            'role': 'employee',  # Use a valid role
        }, format='json')

        # Attempt to register the same user again
        response = self.client.post(url, {
            'username': 'existinguser',
            'email': 'existinguser@example.com',
            'password': 'password123',
            'role': 'employee',  # Use a valid role
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', response.data)
        self.assertIn('username', response.data['errors'])
        self.assertEqual(response.data['errors']['username'], ["A user with that username already exists."])
