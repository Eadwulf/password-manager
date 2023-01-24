from django.db import models
from django.urls import reverse

from accounts.models import User


class Website(models.Model):
    url = models.URLField(max_length=64)
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='website')

    def get_absolute_url(self):
        return reverse('website_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
