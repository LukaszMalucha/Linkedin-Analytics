from django.contrib import admin
from django.urls import path, include

from dashboard.views import error_404, error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('api/', include('api.urls')),
    path('insights/', include('insights.urls')),
]


handler404 = error_404
handler500 = error_500