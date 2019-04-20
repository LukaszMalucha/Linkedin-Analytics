from django.shortcuts import render
from .utils import database_upload, sector_insights, sector_listing, find_company
from core.models import Company

import re


def companies(request, sector):
    # If needed for database
    # database_upload()
    try:
        context = sector_insights(sector)
    except:
        return render(request, "dashboard.html")

    return render(request, "insights.html", context)


def listing(request, sector):
    
    try:
        context = sector_listing(sector)
    except:    
        return render(request, "dashboard.html")
        
    return render(request, "listing.html", context)


def company_search(request):
    
    try:
        context = find_company(request.GET['query'])
    except:
        return render(request, "dashboard.html")

    return render(request, "company_search.html", context)
