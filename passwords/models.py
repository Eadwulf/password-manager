from django.db import models

from accounts.models import CustomUser

from hashlib import sha256


SMALL_TEXT       =  32
MEDIUM_TEXT      =  64
LARGE_TEXT       = 128
EXTRA_LARGE_TEXT = 256


class Password(models.Model):
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='associated_passwords')
    username = models.CharField(max_length=SMALL_TEXT)
    password_hash = models.CharField(max_length=MEDIUM_TEXT)
    website = models.ForeignKey('passwords.Website', on_delete=models.CASCADE, related_name='associated_passwords')
    add_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    def get_hash(self, string):
        return sha256(string.encode('utf-8')).hexdigest()

    def __str__(self):
        if len(self.website.name) > 0:
            output = self.website.name
        elif len(self.website.url) > 0:
            output = self.website.url 
        return f'Password for {output}'


class Website(models.Model):
    name = models.CharField(max_length=MEDIUM_TEXT)
    url = models.SlugField(max_length=MEDIUM_TEXT, blank=True, null=True)
    description = models.CharField(max_length=EXTRA_LARGE_TEXT, blank=True, null=True)
