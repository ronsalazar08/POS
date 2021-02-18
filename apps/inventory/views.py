import json
from django.http import JsonResponse
from django.core import serializers

from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *


def inventory(request):
    products = Product.objects.all()
    list_of_needed_prod = products.filter(qty_stock__lte=4).order_by('name')
    form = ProductForm()
    if request.method == "POST":
        form_ctrl = request.POST.get('form_ctrl')
        if form_ctrl == "new_item":
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Item <span class="text-primary">{form.cleaned_data["name"].upper()}</span> Successfully Added!')
                return redirect('inventory')
        else:
            pk = form_ctrl
            form = ProductForm(request.POST, instance=Product.objects.get(pk=pk))
            if form.is_valid():
                form.save()
                messages.success(request, f'Item <span class="text-primary">{form.cleaned_data["name"].upper()}</span> Successfully Updated!')
                return redirect('inventory')
    context = {
        'products' : products,
        'form'  : form,
        'list_of_needed_prod' : list_of_needed_prod,
    }
    return render(request, 'inventory/inventory.html', context)


def delete_product(request, pk):
    try:
        prod = Product.objects.get(pk=pk)
        Product.objects.get(pk=pk).delete()
        messages.success(request, f' <span class="text-primary">{prod.name.upper()}</span> Successfully Deleted!')
    except:
        messages.warning(request, f"Product Don't exist!")
    
    return redirect('inventory')


def get_product(request, barcode):
    try:
        prod = Product.objects.get(barcode=barcode)
        data = serializers.serialize('json', [prod,])
        struct = json.loads(data)
        data = json.dumps(struct[0])
        return HttpResponse(data)
    except:
        return HttpResponse({'info': False})