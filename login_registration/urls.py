from django.urls import path
from . import views

app_name = 'login_registration'

urlpatterns = [
    path('register', views.SignUpView.as_view(), name='register_new_user'),
    ]
