from django.urls import path

from .views import credential_list, credential_detail


urlpatterns = [
    path('credentials', credential_list, name='credential_list'),
    path('credentials/<int:pk>', credential_detail, name='credential_detail'),
]