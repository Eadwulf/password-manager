from django import forms

from passwords.models import Password


class PasswordCreateForm(forms.ModelForm):

    class Meta:
        model = Password
        fields = '__all__'
    