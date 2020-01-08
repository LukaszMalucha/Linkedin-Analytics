from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.serializers import CompanySerializer
from core.models import Company

COMPANIES_URL = reverse("api:companies-list")
FINANCE_URL = reverse("api:finance-list")
IT_URL = reverse("api:it-list")
EDUCATION_URL = reverse("api:education-list")
FINANCIAL_INSIGHTS_URL = reverse("api:financial-insights")
IT_INSIGHTS_URL = reverse("api:it-insights")
EDUCATION_INSIGHTS_URL = reverse("api:education-insights")



class CompaniesApiTests(TestCase):
    """Test the publicly available companies API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_companies_list(self):
        """Test retrieving companies list"""
        Company.objects.create()
        Company.objects.create(
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

        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        response = self.client.get(COMPANIES_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_create_company_successful(self):
        """Test create new company by admin user"""
        self.superuser = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test Company"}
        self.client.post(COMPANIES_URL, payload)

        exist = Company.objects.filter(
            name=payload['name'],
        ).exists()
        self.assertTrue(exist)


class FinanceViewTests(TestCase):
    """Test Financial companies viewset"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_finance_view(self):
        """Accessing financial companies view"""
        response = self.client.get(FINANCE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_financial_company_successful(self):
        """Test creating financial company"""

        self.superuser = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test Company"}
        self.client.post(FINANCE_URL, payload)

        exist = Company.objects.filter(
            name=payload['name'],
        ).exists()
        self.assertTrue(exist)


class ITViewTest(TestCase):
    """Test IT companies viewset"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_it_view(self):
        """Accessing IT companies view"""
        response = self.client.get(IT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_it_company_successful(self):
        """Test creating IT company"""

        self.superuser = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test Company"}
        self.client.post(IT_URL, payload)

        exist = Company.objects.filter(
            name=payload['name'],
        ).exists()
        self.assertTrue(exist)


class EducationViewTest(TestCase):
    """Test IT companies viewset"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_it_view(self):
        """Accessing education companies view"""
        response = self.client.get(EDUCATION_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_education_company_successful(self):
        """Test creating education company"""

        self.superuser = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test Company"}
        self.client.post(EDUCATION_URL, payload)

        exist = Company.objects.filter(
            name=payload['name'],
        ).exists()
        self.assertTrue(exist)


class FinancialInsightsView(TestCase):
    """Test Financial Insight view"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_financial_insights_view(self):
        """Accessing Financial Insight view"""
        response = self.client.get(FINANCIAL_INSIGHTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sector_strings'], ['Financial Companies', 'finance'])


class ITInsightsView(TestCase):
    """Test Financial Insight view"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_it_insights_view(self):
        """Accessing Financial Insight view"""
        response = self.client.get(IT_INSIGHTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sector_strings'], ['IT Companies', 'it'])


class EducationInsightsView(TestCase):
    """Test Financial Insight view"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_education_insights_view(self):
        """Accessing Financial Insight view"""
        response = self.client.get(EDUCATION_INSIGHTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sector_strings'], ['Educational Institutions', 'education'])
