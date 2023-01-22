from django.contrib import admin

from passwords.models import Password, Website

admin.site.register(Password)
admin.site.register(Website)
