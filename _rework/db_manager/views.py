from django.shortcuts import render
from db_manager.utils import database_upload, sector_insights


def db_upload(request):
    """ Uncomment if needed"""
    # database_upload()
    return render(request, 'index.html')

def sector_upload(request):
    """Sector insights"""
    sector_insights('finance')
    return render(request, 'index.html')