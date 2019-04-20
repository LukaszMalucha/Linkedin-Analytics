from django.urls import path
from insights import views

app_name = 'insights'

urlpatterns = [
    path('companies/<str:sector>', views.companies, name='companies'),
    path('list/<str:sector>', views.listing, name='listing'),
    path('company_search', views.company_search, name="company_search")

]
