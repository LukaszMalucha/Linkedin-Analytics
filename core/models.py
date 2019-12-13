from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


# Manager Class
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError(_('User must have a valid email address'))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Model Class
class User(AbstractBaseUser, PermissionsMixin):
    """Customized user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Company(models.Model):

    class Meta:
        verbose_name_plural = "Companies"

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

    def __str__(self):
        return self.name
