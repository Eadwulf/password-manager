from django.views.generic import ListView, CreateView, DetailView

from passwords.models import Password

from passwords.forms import CreatePasswordForm


class PasswordListView(ListView):
    model = Password
    context_object_name = 'passwords'
    template_name = 'passwords/list_view.html'


class PasswordDetailView(DetailView):
    model = Password
    context_object_name = 'password'
    template_name = 'passwords/detail_view.html'


class PasswordCreateView(CreateView):
    form_class = CreatePasswordForm
    template_name = 'passwords/create_view.html'