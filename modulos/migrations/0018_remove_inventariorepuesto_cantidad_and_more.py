# Generated by Django 4.2.5 on 2023-10-17 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0017_alter_inventariovehiculo_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventariorepuesto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='inventariorepuesto',
            name='sucursal',
        ),
    ]
