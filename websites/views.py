from django.views.generic import ListView, CreateView, DetailView

from websites.models import Website

from websites.forms import CreateWebsiteForm


class WebsiteListView(ListView):
    model = Website
    context_object_name = 'websites'
    template_name = 'websites/list_view.html'


class WebsiteDetailView(DetailView):
    model = Website
    context_object_name = 'website'
    template_name = 'websites/detail_view.html'


class WebsiteCreateView(CreateView):
    form_class = CreateWebsiteForm
    template_name = 'websites/create_view.html'