from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer, CredentialSerializer, WebsiteSerializer

from accounts.models import User
from credentials.models import Credential
from websites.models import Website


class UserListView(ListCreateAPIView):
    # TODO: Fix id not null constraint
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
