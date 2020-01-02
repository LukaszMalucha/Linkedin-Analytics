from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('companies', views.CompaniesViewSet, basename='companies')
router.register('finance-list', views.FinanceViewSet, basename='finance')
router.register('it-list', views.ITViewSet, basename='it')
router.register('education-list', views.EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls)),
    path('finance/', views.FinanceInsightsViewSet.as_view(), name="financial-insights"),
    path('it/', views.ITInsightsViewSet.as_view(), name="it-insights"),
    path('education/', views.EducationInsightsViewSet.as_view(), name="education-insights")
]
