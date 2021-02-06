from django.contrib import messages
from django.db.models import Q
from django.http.response import StreamingHttpResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect

from .models import *

class InventoryView(ListView):
    model = Product
    template_name = 'inventory/inventory.html'  
    context_object_name = 'products' 

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)
        context.update({
            # 'form'  : NewDrForm,
            'search' : self.request.GET.get('search'),
        })
        return context
        
    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search')

        queryset = self.model.objects.all().order_by('name')
        if search:
            queryset = queryset.filter(Q(barcode__contains=search) | Q(name__contains=search) | Q(description__contains=search))
            if len(queryset) == 0:
                queryset = self.model.objects.all()
                messages.warning(self.request, f'Cannot find "{search}"')
            else:
                messages.success(self.request, f'Displaying "{search}"')

        return queryset