from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["barcode", "name", "description", "size", "qty_stock", "price"]
    search_fields=["barcode", "name"]