# authentication/urls.py
from django.urls import path,include
from .views import signup, login, CustomSignupView, home


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('account/', include('allauth.urls')),
]
