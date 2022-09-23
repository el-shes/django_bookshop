from django.urls import path, reverse_lazy
from . import views

app_name = 'users'


urlpatterns = [
    path('create_user', views.CreateUserView.as_view(), name='user_create'),
]
