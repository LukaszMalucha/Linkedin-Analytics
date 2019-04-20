from django.urls import path, reverse_lazy
from .views import login, logout, register
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView, \
    PasswordResetCompleteView


app_name='user'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('password-reset/', PasswordResetView.as_view(success_url = reverse_lazy('user:password_reset_done')), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
