from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib import auth, messages
from django.urls import reverse
from django.template.context_processors import csrf

def index(request):
    """A view the returns the index page"""
    return (request, 'index.html')

def user_login(request):
    """View that returns the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                        password=request.POST['password'])
            print(user)
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password is incorrect")
    else:
        user_form = UserLoginForm()
    # Have to use an instance of the model in this bit
    return render(request, 'login.html', {'login_form':user_form})

def user_profile(request):
    return render(request, 'profile.html')