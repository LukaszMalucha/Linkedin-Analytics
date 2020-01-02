from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

from core.permissions import IsAdminOrReadOnly

COMPANIES_URL = reverse("api:companies-list")

class TestIsAdminOrReadOnly(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.user_superuser = get_user_model().objects.create_superuser(
            email="superuser@gmail.com",
            password="test1234",
        )
        self.permission = IsAdminOrReadOnly()


    def test_superuser_has_no_admin_or_read_only_permission(self):
        admin_permission = self.user_superuser.has_perm(IsAdminOrReadOnly)
        self.assertTrue(admin_permission)

    def test_user_has_no_admin_or_read_only_permission(self):
        admin_permission = self.user.has_perm(IsAdminOrReadOnly)
        self.assertFalse(admin_permission)

    def test_user_cant_access_unsafe_methods(self):
        payload = {}
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        response = self.client.post(COMPANIES_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_access_safe_methods(self):
        payload = {}
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        response = self.client.get(COMPANIES_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_can_access_unsafe_methods(self):
        payload = {}
        self.client = APIClient()
        self.client.force_authenticate(user=self.user_superuser)
        response = self.client.post(COMPANIES_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

