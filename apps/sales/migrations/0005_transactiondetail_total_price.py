# Generated by Django 3.1.5 on 2021-03-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20210308_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiondetail',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
