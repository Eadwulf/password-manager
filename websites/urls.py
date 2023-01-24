from django.urls import path

from websites.views import (
    WebsiteListView, WebsiteCreateView, WebsiteDetailView,
)


# app_name = 'websites'
urlpatterns = [
    path('', WebsiteListView.as_view(), name='website_list'),
    path('create/', WebsiteCreateView.as_view(), name='website_create'),
    path('details/<int:pk>/', WebsiteDetailView.as_view(), name='website_detail'),
]