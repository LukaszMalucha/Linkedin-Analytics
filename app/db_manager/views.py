from django.shortcuts import redirect

from db_manager.utils import database_upload, sector_insights


def db_upload(request):
    """Uncomment if refreshing data needed"""
    database_upload()
    return redirect('/')


def sector_upload(request):
    """Uncomment if refreshing data needed"""
    sector_insights('finance')
    sector_insights('it')
    sector_insights('education')
    return redirect('/')
