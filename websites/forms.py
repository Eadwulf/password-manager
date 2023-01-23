
from django import forms

from websites.models import Website


class CreateWebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = '__all__'
    
    def clean_url(self):
        return self.cleaned_data['url'].lower()