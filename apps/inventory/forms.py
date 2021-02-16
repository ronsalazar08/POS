from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["barcode", "name", "description", "size", "qty_stock", "price"]

