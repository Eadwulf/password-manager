from django.db import models
from django.urls import reverse


SMALL_TEXT       =  32
MEDIUM_TEXT      =  64
LARGE_TEXT       = 128
EXTRA_LARGE_TEXT = 256


class Website(models.Model):
    url = models.URLField(max_length=MEDIUM_TEXT)
    name = models.CharField(max_length=MEDIUM_TEXT, blank=True, null=True)
    description = models.CharField(max_length=EXTRA_LARGE_TEXT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('website_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
