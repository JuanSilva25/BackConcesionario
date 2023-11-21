# Generated by Django 4.2.6 on 2023-10-16 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0024_remove_venta_idusuario_remove_venta_vendedor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='nombreVehiculo',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='vehiculoId',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='ventaId',
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='vehiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.vehiculo'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.venta'),
        ),
    ]