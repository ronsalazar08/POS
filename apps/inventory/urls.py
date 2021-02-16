from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.inventory), name='inventory'),
    path('delete/<int:pk>', login_required(views.delete_product), name='delete_product'),
    path('get_product/<int:barcode>', login_required(views.get_product), name='get_product'),
]
