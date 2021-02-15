from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *
from .forms import *


def inventory(request):
    products = Product.objects.all()
    form = ProductForm()
    category_form = CategoryForm()
    if request.method == "POST":
        form_ctrl = request.POST.get('form_ctrl')
        if form_ctrl == "new_item":
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Item <span class="text-primary">{form.cleaned_data["name"].upper()}</span> Successfully Added!')
                return redirect('inventory')
        elif form_ctrl == "new_category":
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                form.save()
                messages.success(request, f'Category <span class="text-primary">{form.cleaned_data["name"].upper()}</span> Successfully Added!')
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
        'category_form'  : category_form,
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