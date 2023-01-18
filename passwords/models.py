from django.db import models

from accounts.models import CustomUser


class Password(models.Model):
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=64)
    website = models.ForeignKey('passwords.Website', on_delete=models.CASCADE)
    add_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)


class Website:
    name = models.CharField(max_length=64)
    url = models.SlugField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    