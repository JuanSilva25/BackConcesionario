# Generated by Django 4.2.5 on 2023-11-20 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0054_alter_detalleventa_cantidad_repuesto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='cantidad_repuesto',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='total_repuesto',
        ),
    ]
