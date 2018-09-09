from django.urls import path
from .views import all_prints

urlpatterns = [
    path('', all_prints, name='prints'),
]
