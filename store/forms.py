from django import forms
from django.forms import ModelForm
from .models import Adresa

# class AdresaForm(forms.Form):
#     nume = forms.CharField(max_length=100)
#     judet = forms.CharField(max_length=100)
#     localitate = forms.CharField(max_length=100)
#     strada = forms.CharField(max_length=100)
#     numar = forms.CharField(max_length=100)
#     bloc = forms.CharField(max_length=100)
#     scara = forms.CharField(max_length=100)
#     ap = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length = 200)
#     telefon = forms.CharField(max_length=100)
#     cantitate = forms.IntegerField()


class AdresaForm(ModelForm):
    class Meta:
        model = Adresa
        fields = ['nume', 'judet', 'localitate', 'strada', 'numar', 'bloc', 'scara', 'ap', 'email', 'telefon', 'cantitate']
