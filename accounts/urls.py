"""
Here we want to include URLS for the index.html, profile and login page
for index.html we want to got a url of acccounts/ to render the index.html page
for /login we want to go to the login page and for registration we want to go to the 
registration.html

step 1 import the url module
we need to import the views that take us to where we need to go
"""
from django.urls import path
from .views import user_login, user_profile

urlpatterns = [
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile')
]