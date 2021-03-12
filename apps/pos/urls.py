from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.pos), name='pos'),
    path('api_all_product/', login_required(views.api_all_product), name='api_all_product'),
    path('post_new_edit_product/', login_required(views.post_new_edit_product), name='post_new_edit_product'),
]
