from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.InventoryView.as_view()), name='inventory'),
    path('delete/<int:pk>', login_required(views.delete_product), name='delete_product'),
]
