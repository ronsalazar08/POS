from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.inventory), name='inventory'),
    # path('delete/<int:pk>', login_required(views.delete_employee), name='delete_employee'),
]
