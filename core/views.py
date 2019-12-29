from django.views.generic.base import TemplateView
from django.shortcuts import render

class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name

def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


