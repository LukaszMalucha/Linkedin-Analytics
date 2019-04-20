from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard.html")


def rest(request):
    return render(request, "rest.html")


def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
