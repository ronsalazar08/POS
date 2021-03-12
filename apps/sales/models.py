from django.db import models

class Transaction(models.Model):
    date_time = models.DateTimeField()
    amount_sale = models.FloatField(default=0)
    amount_recieved = models.FloatField(default=0)
    amount_changed = models.FloatField(default=0)
    employee = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("transaction")
        verbose_name_plural = ("transactions")

    def __str__(self):
        return str(self.id)


class TransactionDetail(models.Model):
    barcode = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    qty = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    transaction = models.ForeignKey(Transaction, to_field="id", db_column="pk", on_delete=models.CASCADE, default='', related_name='entries')

    class Meta:
        verbose_name = ("transactiondetail")
        verbose_name_plural = ("transactiondetails")

    def __str__(self):
        return self.barcode