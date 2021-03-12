import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from apps.sales.models import *
from apps.inventory.models import *

def home_sales(request):
    return HttpResponse("OLO")


def post_transaction(request):
    try:
        data = json.loads(request.body)
        trans = Transaction(**data[-1])
        trans.save()
        print(data)
        for o in data[:-1]:
            print(o)
            prod = TransactionDetail(
                barcode=o["barcode"],
                name=o["name"],
                size=o["size"],
                qty=o["qty"],
                price=o["price"],
                total_price=o["total_price"],
                transaction=trans
            )

            product_inv = Product.objects.get(barcode=o["barcode"])
            new_qty = product_inv.qty_stock - int(o["qty"])
            product_inv.qty_stock = 0 if new_qty <= 0 else new_qty
            
            product_inv.save()
            prod.save()
        return JsonResponse({'success': True})
    except:
        return JsonResponse({'success': False})