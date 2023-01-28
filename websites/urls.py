from django.urls import path

from websites.views import (
    BasicCreateView,
    WebsiteListView, WebsiteCreateView, WebsiteDetailView,
    ListJsonView,
)


# app_name = 'websites'
urlpatterns = [
    path('', WebsiteListView.as_view(), name='website_list'),
    path('create/', BasicCreateView.as_view(), name='website_create'),
    # path('create/', WebsiteCreateView.as_view(), name='website_create'),
    path('details/<int:pk>/', WebsiteDetailView.as_view(), name='website_detail'),
    path('json/', ListJsonView.as_view(), name='json')
]