from django.urls import path

from credentials.views import (
    CredentialListView, CredentialCreateView, CredentialDetailView,
)


# app_name = 'credential'
urlpatterns = [
    path('', CredentialListView.as_view(), name='credential_list'),
    path('create/', CredentialCreateView.as_view(), name='credential_create'),
    path('details/<int:pk>/', CredentialDetailView.as_view(), name='credential_detail'),

]