from django.urls import path, re_path
from .views import originals, submit_bid

urlpatterns = [
    path('', originals, name='auction'),
    re_path(r'^bid/(?P<id>\d+)', submit_bid, name='submit_bid'),
]