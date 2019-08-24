# Generated by Django 2.2.2 on 2019-08-24 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190823_2132'),
        ('serials', '0004_auto_20190823_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serial',
            name='aircraft',
        ),
        migrations.AddField(
            model_name='serial',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]
