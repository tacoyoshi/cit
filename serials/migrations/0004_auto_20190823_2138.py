# Generated by Django 2.2.2 on 2019-08-24 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0003_auto_20190823_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serial',
            options={'ordering': ['serial_number']},
        ),
    ]
