import json
from django.http import JsonResponse
from django.shortcuts import render

from apps.inventory.models import *

def pos(request):
    context = {
    }
    return render(request, 'pos/pos.html', context)


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