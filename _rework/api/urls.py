from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('companies', views.CompaniesViewSet, basename='companies')
router.register('finance', views.FinanceViewSet, basename='finance')
router.register('it', views.ITViewSet, basename='it')
router.register('education',views.EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls)),
]
