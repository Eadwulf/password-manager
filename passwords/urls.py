from django.urls import path

from passwords.views import PasswordListView


appname = 'passwords'
urlpatterns = [
    path('', PasswordListView.as_view(), name='passwordlist'),
]