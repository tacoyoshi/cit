# Generated by Django 2.2.4 on 2019-08-27 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190827_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_code'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
