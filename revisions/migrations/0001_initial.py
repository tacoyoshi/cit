# Generated by Django 2.2.4 on 2019-08-27 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serials', '0007_auto_20190827_1014'),
        ('projects', '0003_auto_20190823_2137'),
        ('parts', '0001_initial'),
        ('options', '0003_auto_20190823_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_number', models.CharField(max_length=12, verbose_name='Revision')),
                ('rev_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('rev_effective', models.DateField(blank=True, verbose_name='Effective Date')),
                ('rev_ed_code', models.CharField(max_length=8, verbose_name='ED Code')),
                ('rev_description', models.CharField(max_length=200, verbose_name='Description')),
                ('rev_notes', models.TextField(blank=True, verbose_name='Revision Notes')),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='options.Option', verbose_name='Option')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.Part', verbose_name='Part')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project', verbose_name='Project')),
                ('serial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='serials.Serial', verbose_name='Serial Effectivity')),
            ],
        ),
    ]
