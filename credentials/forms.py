from django import forms

from credentials.models import Credential


class CredentialCreateForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = '__all__'