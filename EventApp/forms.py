from  django import forms
from EventApp.models import Place, Type


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
