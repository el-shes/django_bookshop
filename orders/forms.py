from django import forms
from .models import CustomerOrder


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ('customer', 'ordered_books')

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'ordered_books': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
