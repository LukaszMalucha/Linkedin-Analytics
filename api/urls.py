from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('companies', views.CompaniesViewSet, basename='companies')


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('authenticate/', views.CreateTokenView.as_view(), name='authenticate'),
    path('my_account/', views.ManageUserView.as_view(), name='my_account'),
    path('', include(router.urls)),
]
