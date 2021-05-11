from django import forms
from filmy.models import Person, Movie
# class Person(models.Model):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
from django.core.exceptions import ValidationError


def check_if_big(kielbaska):
    if kielbaska[0].isupper():
        raise ValidationError("Musi być wieką literą")


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=16)
    last_name = forms.CharField(max_length=16)

    def clean(self):
        data = super().clean()
        first_name = data['first_name']
        last_name = data['last_name']
        if len(first_name) + len(last_name) > 16:
            raise ValidationError("poszły ptaki na spacer")
        return data


class MovieForm(forms.Form):
    title = forms.CharField(max_length=128)
    director = forms.ModelChoiceField(queryset=Person.objects.all())


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        #fields = ['year', 'title']
        exclude = ['category']


