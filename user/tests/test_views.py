from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

CREATE_USER_URL = reverse("user:register")
LOGIN_USER_URL = reverse("user:login")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserTests(TestCase):
    """Test views that don't require authentication"""

    def setUp(self):
        self.client = Client()

    def test_get_register_page(self):
        """Test that login page is accessible"""
        page = self.client.get(CREATE_USER_URL)
        self.assertEqual(page.status_code, 200)

    def test_get_login_page(self):
        """Test that register page is accessible"""
        page = self.client.get(LOGIN_USER_URL)
        self.assertEqual(page.status_code, 200)

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""

        payload = {
            "email": "test@gmail.com",
            "password1": "test@1234567",
            "password2": "test@1234567",
            "name": "Test name"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, 201)
        user = get_user_model().objects.get(**res.data)
        # self.assertTrue(user.check_password(payload["password"]))
        # self.assertNotIn("password", res.data)


