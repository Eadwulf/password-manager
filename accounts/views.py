from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from accounts.forms import UserCreationForm


class AccountsSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'