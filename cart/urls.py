from django.urls import re_path, path, include, reverse_lazy
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name="view_cart"),
    re_path(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    re_path(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]