from django import forms
from .models import firstVariety

class firstVarietyForm(forms.Form):
    first_variety = forms.ModelChoiceField(queryset=firstVariety.objects.all(), label = 'Select a first variety')

    

