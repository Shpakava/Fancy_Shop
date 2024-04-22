from django.test import TestCase, Client
from django.contrib.auth.models import User
import pytest
from django.urls import reverse

# Create your tests here.

class TestProfile(TestCase):

    @pytest.mark.django_db
    def setUp(self) -> None:
        self.client = Client()
        self.credentials = {
            "username": "testuser",
            "password": "t954_yI08!",
            "email": "test@test.com"
        }
        self.user = User.objects.create_user(self.credentials)


    def test_authentication(self):
        self.client.force_login(self.user)
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 301)


    def test_register_url(self):
        self.client.logout()
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)


    def test_view(self):
        self.client.force_login(self.user)
        url = reverse("profile_details", kwargs={"profile_slug": "test-user"})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)