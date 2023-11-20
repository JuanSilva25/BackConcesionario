# Generated by Django 4.2.5 on 2023-11-20 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0053_rename_preciounitario_detalleventa_total_repuesto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad_repuesto',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad_vehiculo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='total_repuesto',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='total_vehiculo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='precioTotal',
            field=models.FloatField(max_length=100),
        ),
    ]
