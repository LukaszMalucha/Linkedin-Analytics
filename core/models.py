from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import os

# Manager Class
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError(('User must have a valid email address'))
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

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        user_profile = MyProfile.objects.filter(owner=self).first()
        if not user_profile:
            user_profile = MyProfile(owner=self, position="guest", username=self.name)
            user_profile.save()


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.owner.id, "portrait", ext)
    return os.path.join('portraits', filename)


class MyProfile(models.Model):
    """User Profile Details"""
    username = models.CharField(max_length=254, default='Anonymous', blank=True)
    position = models.CharField(max_length=254, default='guest', blank=True)
    image = models.ImageField(upload_to=content_file_name, default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"


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
