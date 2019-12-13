import os
import json
from django.conf import settings
from rest_framework import generics, authentication, permissions, viewsets, status, filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from user.api.serializers import UserSerializer, AuthTokenSerializer
from core.permissions import IsAdminOrReadOnly
from api import serializers
from core.models import Company

finance_sector = os.path.join(settings.BASE_DIR, "db_manager/datasets/finance.json")
it_sector = os.path.join(settings.BASE_DIR, "db_manager/datasets/it.json")
education_sector = os.path.join(settings.BASE_DIR, "db_manager/datasets/education.json")



class CompaniesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, IsAdminOrReadOnly)
    serializer_class = serializers.CompanySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "companyType", "industries", "specialities", "group")
    ordering_fields = '__all__'
    queryset = Company.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-name')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinanceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, IsAdminOrReadOnly)
    serializer_class = serializers.CompanySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "companyType", "industries", "specialties", "group")
    ordering_fields = '__all__'
    queryset = Company.objects.filter(group="finance")

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('name')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ITViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, IsAdminOrReadOnly)
    serializer_class = serializers.CompanySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "companyType", "industries", "specialties", "group")
    ordering_fields = '__all__'
    queryset = Company.objects.filter(group="it")

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('name')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, IsAdminOrReadOnly)
    serializer_class = serializers.CompanySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "companyType", "industries", "specialties", "group")
    ordering_fields = '__all__'
    queryset = Company.objects.filter(group="education")

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('name')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinanceInsightsViewSet(APIView):

    def get(self, request):
        sector_file = open(finance_sector)
        sector_str = sector_file.read()
        sector_data = json.loads(sector_str)
        return Response(sector_data)


class ITInsightsViewSet(APIView):

    def get(self, request):
        sector_file = open(it_sector)
        sector_str = sector_file.read()
        sector_data = json.loads(sector_str)
        return Response(sector_data)


class EducationInsightsViewSet(APIView):

    def get(self, request):
        sector_file = open(education_sector)
        sector_str = sector_file.read()
        sector_data = json.loads(sector_str)
        return Response(sector_data)
