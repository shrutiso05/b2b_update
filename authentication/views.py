# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignupForm, LoginForm
from .models import UserProfile
from django.db import IntegrityError 
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    template_name = 'signup.html'

    def form_valid(self, form):
        # Call the parent class's form_valid method to handle the actual signup
        response = super().form_valid(form)

        # Custom actions to perform after successful signup
        # For example, you can send a welcome email or redirect to a specific page
        self.send_welcome_email(self.request.user.email)
        return response

    def send_welcome_email(self, email):
        # Implement your logic to send a welcome email
        # You can use Django's built-in EmailMessage or other third-party packages

        # For example using Django's built-in EmailMessage:
        from django.core.mail import EmailMessage

        subject = 'Welcome to Your Website'
        message = 'Thank you for signing up!'
        to_email = [email]

        email = EmailMessage(subject, message, to=to_email)
        email.send()




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                return redirect('login')
            except IntegrityError:
                form.add_error('business_email', 'Email already exists. Please choose another.')
        else:
            # Handle invalid form
            pass
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

# authentication/views.py

def home(request):
    return render(request, 'home.html')



# Create your views here.
