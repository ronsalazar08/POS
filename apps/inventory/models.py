from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)    

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    barcode = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)    
    qty_stock = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    encoded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name