from django import forms
from .models import CardInfo
from django.forms import formset_factory

class CardInfoForm(forms.Form):
    card_name = forms.CharField (
        max_length=100,
        label="Card Name",
        widget=forms.TextInput(attrs={"placeholder": "e.g. My Savings Card"})
    )
    savings = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Savings Amount",
        widget=forms.NumberInput(attrs={"placeholder": "e.g. 500.00"})
    )

    checking = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Checking Amount",
        widget=forms.NumberInput(attrs={"placeholder": "e.g. 200.00"})
    )
   