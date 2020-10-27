from django.test import TestCase

from core.models import Company
from db_manager.utils import database_upload


class DatabaseUploadTests(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test",
            companyType="test",
            employeeCountRange="12",
            foundedYear="test",
            industries="test",
            numFollowers="12",
            specialities="test",
            squareLogoUrl="test.jpg",
            websiteUrl="www.test.com",
            group="test",
        )
        self.empty_company = Company.objects.create()

    def tearDown(self):
        self.company.delete()
        self.empty_company.delete()

    def test_function_deletes_previous_companies(self):
        """Test that db is cleaned before the upload"""
        database_upload()
        self.assertEqual(len(Company.objects.filter(name="Test")), 0)
        self.assertEqual(len(Company.objects.filter(name="Undisclosed")), 0)













