from django import forms
from django.conf import settings


PRODUCTS_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, settings.MAX_CART_ITEMS + 1)]

# (1, "1")

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCTS_QUANTITY_CHOICES,
        coerce=int
    )
    override_quantity = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )