from websites.models import Website
from websites.forms import WebsiteCreateForm
from utils.views import CreateViewMixin, DetailViewMixin, ListViewMixin


class WebsiteCreateView(CreateViewMixin):
    form_class = WebsiteCreateForm
    template_name = 'websites/create_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class WebsiteListView(ListViewMixin):
    model = Website
    context_object_name = 'websites'
    template_name = 'websites/list_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class WebsiteDetailView(DetailViewMixin):
    model = Website
    context_object_name = 'website'
    template_name = 'websites/detail_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'