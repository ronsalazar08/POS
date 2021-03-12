from django.contrib import admin
from .models import Transaction, TransactionDetail


@admin.register(Transaction)
class ProductAdmin(admin.ModelAdmin):
    list_display=["id", "date_time", "amount_sale", "amount_recieved", "amount_changed", "employee", ]
    search_fields=["date_time"]


@admin.register(TransactionDetail)
class ProductAdmin(admin.ModelAdmin):
    list_display=["transaction", "barcode", "name", "size", "qty", "price", "total_price"]
    search_fields=["transaction"]
    raw_id_fields = ['transaction',]