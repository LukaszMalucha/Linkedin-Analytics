from django.test import TestCase

from db_manager.apps import DbManagerConfig


class CoreConfigAppTests(TestCase):

    def test_app_name(self):

        self.assertEqual(DbManagerConfig.name, "db_manager")
