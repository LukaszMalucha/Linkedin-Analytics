from django.shortcuts import render
from .utils import database_upload, sector_insights, sector_listing, find_company
from core.models import Company

import re


def companies(request, sector):
    # If needed for database
    # database_upload()

    context = sector_insights(sector)

    return render(request, "insights.html", context)


def listing(request, sector):
    context = sector_listing(sector)

    return render(request, "listing.html", context)


def company_search(request):

    context = find_company(request.GET['query'])


    return render(request, "company_search.html", context)
