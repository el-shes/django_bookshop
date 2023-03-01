from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .models import User


class ProfilePage(DetailView):
    model = User
    template_name = 'users/profile_page_base.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context['include_section'] = 'overview'
        return context


class EditUserView(UpdateView):
    model = User
    template_name = 'users/profile_page_base.html'
    fields = ['username', 'first_name', 'last_name', 'email']

    def get_context_data(self, **kwargs):
        context = super(EditUserView, self).get_context_data(**kwargs)
        context['include_section'] = 'info_update'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('users:profile_page', kwargs={'pk': self.kwargs['pk']})


class ChangeUserPassword(UpdateView):
    model = User
    template_name = 'users/profile_page_base.html'

    def get_context_data(self, **kwargs):
        context = super(ChangeUserPassword, self).get_context_data(**kwargs)
        context['include_section'] = 'change_password'
        return context
