# Generated by Django 3.1.5 on 2021-03-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_transactiondetail_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiondetail',
            name='barcode',
            field=models.CharField(max_length=50),
        ),
    ]
