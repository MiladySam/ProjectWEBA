from django import forms

class DepenseForm(forms.Form):
    titre = forms.CharField(max_length=100)
    montant  = forms.IntegerField()
    categorie = forms.CharField(max_length=100)