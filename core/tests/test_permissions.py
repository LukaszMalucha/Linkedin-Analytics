from django.test import TestCase, Client
from core.utils import content_file_name
from core.models import MyProfile
from core.permissions import IsAdminOrReadOnly
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model
from unittest.mock import patch, MagicMock


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
        self.request = MagicMock(user=MagicMock())
        self.view = MagicMock()


    def test_superuser_has_no_admin_or_read_only_permission(self):
        admin_permission = self.user_superuser.has_perm(IsAdminOrReadOnly)
        self.assertTrue(admin_permission)

    def test_user_has_no_admin_or_read_only_permission(self):
        admin_permission = self.user.has_perm(IsAdminOrReadOnly)
        self.assertFalse(admin_permission)

