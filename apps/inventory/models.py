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

    def save(self, *args, **kwargs):
        for field_name in ['name', 'description',]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(Product, self).save(*args, **kwargs)