from django import forms
from .models import CardInfo
from django.forms import formset_factory

class CardInfoForm(forms.ModelForm):
    class Meta:
        model = CardInfo
        fields = ['card_name', 'savings_amount', 'checking_amount']
        widgets = {
            'card_name': forms.TextInput(attrs={'class': 'form-control'}),
            'savings_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'checking_amount': forms.NumberInput(attrs={'class': 'form-control'})
        }

CardInfoSet = formset_factory(CardInfoForm, extra=1)