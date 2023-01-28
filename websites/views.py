from django.views import View
from django.shortcuts import render

from websites.models import Website
from websites.forms import WebsiteCreateForm
from utils.views import IsAuthorizedMixin, CreateViewMixin, DetailViewMixin, ListViewMixin

from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse


class WebsiteCreateView(CreateViewMixin):
    form_class = WebsiteCreateForm
    template_name = 'websites/create_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class WebsiteListView(ListViewMixin):
    model = Website
    context_object_name = 'websites'
    template_name = 'websites/list_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'


class WebsiteDetailView(IsAuthorizedMixin, View):
    model = Website
    context_object_name = 'website'
    template_name = 'websites/detail_view.html'
    unauthorized_access_template = 'authentication/unauthorized_access.html'

    def get(self, request, pk, *args, **kwargs):
        if self.user_is_authorized(request):
            website = self.model.objects.get(pk=pk)
            saved_credentials = website.credentials.all()
            context = {'website': website, 'saved_credentials': saved_credentials}
            return render(request, self.template_name, context)
        return render(request, self.unauthorized_access_template)


class BasicCreateView(View):
    form_class = WebsiteCreateForm
    template_name = 'websites/create_view.html'
    
    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            website = Website.objects.create(
                name = self.form_class.cleaned_data.get('name', ''),
                url = self.form_class.cleaned_data.get('url'),
                description = self.form_class.cleaned_data.get('description', ''),
                user = request.user,
            )
            print(form.cleaned_data)
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)


class ListJsonView(View):

    def get(self, request):
        json_response = JsonResponse(model_to_dict(Website))
        if request.method == 'GET':
            return json_response