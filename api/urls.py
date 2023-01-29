from django.urls import path

from .views import (
    CredentialListView, CredentialDetailView,
    WebsiteListView, WebsiteDetailView,
)


urlpatterns = [
    path('credentials', CredentialListView.as_view(), name='credential_list'),
    path('credentials/<int:pk>', CredentialDetailView.as_view(), name='credential_detail'),

    path('websites/', WebsiteListView.as_view()),
    path('websites/<int:pk>', WebsiteDetailView.as_view()),
]