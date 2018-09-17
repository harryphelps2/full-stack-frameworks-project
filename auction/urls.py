from django.urls import path
from .views import originals

urlpatterns = [
    path('', originals, name='auction'),
]