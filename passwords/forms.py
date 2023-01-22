from django import forms

from passwords.models import Password


class CreatePasswordForm(forms.ModelForm):

    class Meta:
        model = Password
        fields = '__all__'
    
    def clean_url(self):
        return self.cleaned_data['url'].lower()