from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView


class IsAuthorizedMixin:

    unauthorized_access_template = ''

    def user_is_authorized(self, request):
        return not(request.user.is_anonymous)


class CreateViewMixin(IsAuthorizedMixin, CreateView):

    def get(self, request, *args, **kwargs):
        if self.user_is_authorized(request):
            return super().get(request, *args, **kwargs)
        return render(request, self.unauthorized_access_template)
    
    def post(self, request, *args, **kwargs):
        if self.user_is_authorized(request):
            return super().post(request, *args, **kwargs)
        return render(request, self.unauthorized_access_template)


class DetailViewMixin(IsAuthorizedMixin, DetailView):
    
    def get(self, request, *args, **kwargs):
        if self.user_is_authorized(request):
            return super().get(request, *args, **kwargs)
        return render(request, self.unauthorized_access_template)


class ListViewMixin(IsAuthorizedMixin, ListView):

    def get(self, request, *args, **kwargs):
        if self.user_is_authorized(request):
            return super().get(request, *args, **kwargs)
        return render(request, self.unauthorized_access_template)