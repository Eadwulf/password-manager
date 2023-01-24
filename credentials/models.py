from django.db import models
from django.urls import reverse

from websites.models import Website


class Credential(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    added_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(blank=True, null=True, default=None)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='saved_credentials')

    def get_absolute_url(self):
        return reverse('credential_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.username} credential'