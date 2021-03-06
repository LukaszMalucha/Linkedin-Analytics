"""linkedin_analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import IndexTemplateView
from django.views.generic import TemplateView

urlpatterns = [
    path('password-reset/confirm/<str:uidb64>/<str:token>', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/', include('user.urls')),
    path('api/', include('api.urls')),
    path('db/', include('db_manager.urls')),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
