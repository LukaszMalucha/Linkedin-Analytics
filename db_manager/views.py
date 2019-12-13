from django.shortcuts import render
from db_manager.utils import database_upload, sector_insights


def db_upload(request):
    """ Uncomment if refreshing data needed"""
    database_upload()
    return render(request, 'index.html')

def sector_upload(request):
    """ Uncomment if refreshing data needed"""
    sector_insights('finance')
    sector_insights('it')
    sector_insights('education')
    return render(request, 'index.html')