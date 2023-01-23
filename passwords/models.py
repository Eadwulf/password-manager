from django.db import models
from django.urls import reverse

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
    website = models.ForeignKey('websites.Website', on_delete=models.CASCADE, related_name='associated_passwords')
    added_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    def get_hash(self, string):
        return sha256(string.encode('utf-8')).hexdigest()
    
    def get_absolute_url(self):
        return reverse('password_detail', kwargs={'pk': self.pk})

    def __str__(self):
            output = self.website.name
            return output