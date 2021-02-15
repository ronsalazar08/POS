from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["name", "description"]
    search_fields=["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["barcode", "name", "description", "size", "qty_stock", "price"]
    search_fields=["barcode", "name", "category"]