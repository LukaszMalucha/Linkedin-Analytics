from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")


def rest(request):
    return render(request, "rest.html")


def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')



# def dashboard(request):
#
#     from django.utils import translation
#     user_language = 'pl'
#     translation.activate(user_language)
#     request.session[translation.LANGUAGE_SESSION_KEY] = user_language