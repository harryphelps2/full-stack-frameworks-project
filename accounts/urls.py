from django.urls import path, include, re_path
from . import urls_reset
from .views import user_login, user_profile
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy

urlpatterns = [
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"), 
]