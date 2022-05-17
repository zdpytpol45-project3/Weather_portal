from django.contrib.auth.forms import UserCreationForm
#from django.forms import ModelForm, TextInput, Form
from django import forms

from .models import City


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}


class LocationForm(forms.Form):
    location = forms.CharField(label='location', max_length=100)