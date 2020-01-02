from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from core.utils import content_file_name


# Manager Class
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('User must have a valid email address')
        if len(str(password)) < 8:
            raise ValueError('This password is too short. It must contain at least 8 characters.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.name = "Admin"
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

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        MyProfile.objects.get_or_create(owner=self)


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
