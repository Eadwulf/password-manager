from django.urls import path

from .views import (
    UserListView, UserDetailView,
    CredentialListView, CredentialDetailView,
    WebsiteListView, WebsiteDetailView,
)


urlpatterns = [
    path('users', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),

    path('credentials', CredentialListView.as_view(), name='credential-list'),
    path('credentials/<int:pk>', CredentialDetailView.as_view(), name='credential-detail'),

    path('websites/', WebsiteListView.as_view(), name='website-list'),
    path('websites/<int:pk>', WebsiteDetailView.as_view(), name='website-detail'),
]