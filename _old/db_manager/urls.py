from django.urls import path

from db_manager import views

app_name = 'db_manager'

urlpatterns = [
    path('db-upload', views.db_upload, name='db-upload'),
    path('sector-upload', views.sector_upload, name='sector-upload')
]
