import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from apps.inventory.models import *

def pos(request):
    context = {
    }
    return render(request, 'pos/pos.html', context)


def api_all_product(request):
    products = Product.objects.all()
    # data = serializers.serialize('json', products)
    data = serializers.serialize('python', products)
    actual_data = [d['fields'] for d in data]
    output = json.dumps(actual_data)
    return HttpResponse(output, content_type="application/json")

def fetch_test(request):
    try:
        data = json.loads(request.body)
        for i in data:
            print(i)
            prod = Product(**i)
            prod.save()
        return JsonResponse({'success': True})
    except:
        return JsonResponse({'success': False})