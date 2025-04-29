from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'email': 'test@example.com', 'name': 'Test User', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

# Add similar tests for Team, Activity, Workout, and Leaderboard
