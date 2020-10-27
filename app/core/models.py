from django.contrib.auth.models import User
from django.db import models

from core.utils import content_file_name


class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default='guest', blank=True)
    image = models.ImageField(upload_to=content_file_name, default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"


class Company(models.Model):
    """Company model for db storage"""
    name = models.CharField(max_length=200, default="Undisclosed", null=True)
    companyType = models.CharField(max_length=200, default="Undisclosed", null=True)
    employeeCountRange = models.CharField(max_length=200, default="Undisclosed", null=True)
    foundedYear = models.CharField(max_length=200, default="Undisclosed", null=True)
    industries = models.TextField(max_length=500, default="Undisclosed", null=True)
    numFollowers = models.CharField(max_length=200, default="Undisclosed", null=True)
    specialities = models.TextField(max_length=1000, default="Undisclosed", null=True)
    squareLogoUrl = models.CharField(max_length=500, default="Undisclosed", null=True)
    websiteUrl = models.CharField(max_length=500, default="Undisclosed", null=True)
    group = models.CharField(max_length=200, default="Undisclosed", null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
