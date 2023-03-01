from django.urls import path, reverse_lazy
from . import views

app_name = 'users'


urlpatterns = [
    path('user/<int:pk>', views.ProfilePage.as_view(), name='profile_page'),
    path('user/<int:pk>/edit_info', views.EditUserView.as_view(), name='edit_profile_page'),
]
