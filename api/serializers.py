from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from core.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Springboard courses"""

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('id',)
