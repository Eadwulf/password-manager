from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # urls for credentials app
    path('credentials/', include('credentials.urls')),

    # urls for websites app
    path('websites/', include('websites.urls')),
]
