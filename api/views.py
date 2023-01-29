from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CredentialSerializer, WebsiteSerializer
from credentials.models import Credential
from websites.models import Website


class CredentialListView(ListCreateAPIView):
    # TODO: Fix id not null constraint
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

class CredentialDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

class WebsiteListView(ListCreateAPIView):
    # TODO: Fix id not null constraint
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

class WebsiteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
