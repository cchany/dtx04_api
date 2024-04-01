# dtx04_api/urls.py
from django.urls import path
from .views import login_api, login_medi_api, Signup_api

urlpatterns = [
    path('Login', login_api, name='login_api'),
    path('Login_Medi', login_medi_api, name='login_medi_api'),
    path('Signup', Signup_api, name='Signup_api'),
]