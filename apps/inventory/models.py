from django.db import models

class Product(models.Model):
    barcode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    size = models.CharField(max_length=50, default='')
    qty_stock = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name