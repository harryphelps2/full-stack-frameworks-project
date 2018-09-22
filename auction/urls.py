from django.urls import path, re_path
from .views import originals, submit_bid, you_win

urlpatterns = [
    path('', originals, name='auction'),
    re_path(r'^bid/(?P<id>\d+)', submit_bid, name='submit_bid'),
    re_path(r'^you_win/', you_win, name='you_win'),
]