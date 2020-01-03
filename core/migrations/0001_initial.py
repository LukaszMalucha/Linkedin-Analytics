# Generated by Django 2.1.5 on 2020-01-03 08:06

import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Undisclosed', max_length=200, null=True)),
                ('companyType', models.CharField(default='Undisclosed', max_length=200, null=True)),
                ('employeeCountRange', models.CharField(default='Undisclosed', max_length=200, null=True)),
                ('foundedYear', models.CharField(default='Undisclosed', max_length=200, null=True)),
                ('industries', models.TextField(default='Undisclosed', max_length=500, null=True)),
                ('numFollowers', models.CharField(default='Undisclosed', max_length=200, null=True)),
                ('specialities', models.TextField(default='Undisclosed', max_length=1000, null=True)),
                ('squareLogoUrl', models.CharField(default='Undisclosed', max_length=500, null=True)),
                ('websiteUrl', models.CharField(default='Undisclosed', max_length=500, null=True)),
                ('group', models.CharField(default='Undisclosed', max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, default='guest', max_length=254)),
                ('image', models.ImageField(default='portraits/default.jpg', upload_to=core.utils.content_file_name)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
