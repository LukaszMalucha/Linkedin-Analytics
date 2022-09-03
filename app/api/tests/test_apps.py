from django.test import TestCase

from api.apps import ApiConfig


class ApiAppTests(TestCase):

    def test_app_name(self):

        self.assertEqual(ApiConfig.name, "api")