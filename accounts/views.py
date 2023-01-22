from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from accounts.forms import CustomUserCreationForm


class AccountsSignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AccountsLoginView(LoginView):
    template_name = 'registration/login.html'