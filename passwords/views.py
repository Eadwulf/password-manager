from django.views.generic import ListView, DetailView

from passwords.models import Password
from passwords.forms import PasswordCreateForm
from passwords.views_mixins import CreateViewMixin


class PasswordCreateView(CreateViewMixin):
    form_class = PasswordCreateForm
    template_name = 'passwords/create_view.html'


class PasswordListView(ListView):
    model = Password
    context_object_name = 'passwords'
    template_name = 'passwords/list_view.html'


class PasswordDetailView(DetailView):
    model = Password
    context_object_name = 'password'
    template_name = 'passwords/detail_view.html'