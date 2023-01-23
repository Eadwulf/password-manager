from django.urls import path

from passwords.views import (
    PasswordListView, PasswordCreateView, PasswordDetailView,
)


appname = 'passwords'
urlpatterns = [
    path('', PasswordListView.as_view(), name='password_list'),
    path('create/', PasswordCreateView.as_view(), name='password_create'),
    path('details/<int:pk>/', PasswordDetailView.as_view(), name='password_detail'),

]