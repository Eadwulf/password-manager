from credentials.models import Credential
from credentials.forms import CredentialCreateForm
from utils.views import CreateViewMixin, DetailViewMixin, ListViewMixin


class CredentialCreateView(CreateViewMixin):
    form_class = CredentialCreateForm
    template_name = 'credentials/create_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class CredentialListView(ListViewMixin):
    model = Credential
    context_object_name = 'credentials'
    template_name = 'credentials/list_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class CredentialDetailView(DetailViewMixin):
    model = Credential
    context_object_name = 'credential'
    template_name = 'credentials/detail_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'