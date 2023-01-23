from django.views.generic import ListView, DetailView

from websites.models import Website
from websites.forms import WebsiteCreateForm

from websites.views_mixins import CreateViewMixin


class WebsiteCreateView(CreateViewMixin):
    form_class = WebsiteCreateForm
    template_name = 'websites/create_view.html'


class WebsiteListView(ListView):
    model = Website
    context_object_name = 'websites'
    template_name = 'websites/list_view.html'


class WebsiteDetailView(DetailView):
    model = Website
    context_object_name = 'website'
    template_name = 'websites/detail_view.html'