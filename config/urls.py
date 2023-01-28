from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    # third party's urls
    path('__debug__/', include('debug_toolbar.urls')),

    # homepage url
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # accounts' urls
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # credentials' urls
    path('credentials/', include('credentials.urls')),

    # websites' urls
    path('websites/', include('websites.urls')),
]
