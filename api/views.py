from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin

from credentials.models import Credential
from websites.models import Website

from .serializers import CredentialSerializer, WebsiteSerializer


class ListViewMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    model_class = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class DetailViewMixin(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    model_class = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CredentialListView(ListViewMixin):
    model_class = Credential
    queryset = model_class.objects.all()
    serializer_class = CredentialSerializer

class CredentialDetailView(DetailViewMixin):
    model_class = Credential
    serializer_class = CredentialSerializer

class WebsiteListView(ListViewMixin):
    model_class = Website
    queryset = model_class.objects.all()
    serializer_class = WebsiteSerializer

class WebsiteDetailView(DetailViewMixin):
    model_class = Website
    serializer_class = WebsiteSerializer
