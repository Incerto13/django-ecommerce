from django import forms
from django.contrib import messages
from shop.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def verify_inventory(self, request, quantity, product):
        if int(quantity) > product.stock:
            messages.error(request, "There is insufficient inventory to fill your order.")
            return False
        else:
            return True
