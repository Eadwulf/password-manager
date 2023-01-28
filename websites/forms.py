from django import forms

from accounts.models import User
from websites.models import Website


class WebsiteCreateForm(forms.Form):
    name = forms.CharField(max_length=64)
    url = forms.URLField(max_length=64)
    description = forms.CharField(max_length=256)
    