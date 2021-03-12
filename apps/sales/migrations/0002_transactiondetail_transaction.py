# Generated by Django 3.1.5 on 2021-03-08 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiondetail',
            name='transaction',
            field=models.ForeignKey(db_column='transaction', default='', on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='sales.transaction'),
        ),
    ]