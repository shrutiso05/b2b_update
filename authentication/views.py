# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignupForm, LoginForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.password = make_password(password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            business_email = form.cleaned_data['business_email']
            password = form.cleaned_data['password']
            user = UserProfile.objects.get(business_email=business_email)
            if check_password(password, user.password):
                # Add login logic here (e.g., set session variables)
                return redirect('home')  # Change 'home' to your home page URL
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# Create your views here.
