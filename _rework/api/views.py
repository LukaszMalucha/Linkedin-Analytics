from rest_framework import generics, authentication, permissions, viewsets, status, filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from user.api.serializers import UserSerializer, AuthTokenSerializer
from core.permissions import IsAdminOrReadOnly
from api import serializers
from core.models import Company


class CompaniesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, IsAdminOrReadOnly)
    serializer_class = serializers.CompanySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "companyType", "industries", "specialties", "group")
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
    queryset = Company.objects.filter(group="Financial")

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-name')

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
    queryset = Company.objects.filter(group="IT")

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-name')

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
    queryset = Company.objects.filter(group="EDUCATION")

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-name')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)