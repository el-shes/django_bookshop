from django.views.generic import CreateView, DetailView
from .models import User


class ProfilePage(DetailView):
    model = User
    template_name = 'users/profile_page_base.html'


class CreateUserView:
    pass
