from passwords.models import Password
from passwords.forms import PasswordCreateForm
from utils.views import CreateViewMixin, DetailViewMixin, ListViewMixin


class PasswordCreateView(CreateViewMixin):
    form_class = PasswordCreateForm
    template_name = 'passwords/create_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class PasswordListView(ListViewMixin):
    model = Password
    context_object_name = 'passwords'
    template_name = 'passwords/list_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class PasswordDetailView(DetailViewMixin):
    model = Password
    context_object_name = 'password'
    template_name = 'passwords/detail_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'