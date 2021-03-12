import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from apps.inventory.models import *

def pos(request):
    return render(request, 'pos/pos.html')


def api_all_product(request):
    products = Product.objects.all()
    # data = serializers.serialize('json', products)
    data = serializers.serialize('python', products)
    actual_data = [d['fields'] for d in data]
    output = json.dumps(actual_data)
    return HttpResponse(output, content_type="application/json")


def post_new_edit_product(request):
    try:
        data = json.loads(request.body)
        # print(data[0])
        # print(data[0]["barcode"])
        try:
            prod = Product.objects.get(barcode=data[0]["barcode"])
            prod.barcode = data[0]["barcode"]
            prod.name = data[0]["name"]
            prod.description = data[0]["description"]
            prod.size = data[0]["size"]
            prod.qty_stock = data[0]["qty_stock"]
            prod.price = data[0]["price"]
            prod.save()
        except:
            prod = Product(**data[0])
            prod.save()
        return JsonResponse({'success': True})
    except:
        return JsonResponse({'success': False})