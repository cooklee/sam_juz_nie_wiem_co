from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, )
    password2 = forms.CharField(widget=forms.PasswordInput, label='re-password')

    def clean(self):
        data = super().clean()
        if data['password'] != data['password2']:
            raise ValidationError("Hasła nie są identyczne")
        return data
