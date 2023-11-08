# Generated by Django 4.2.6 on 2023-10-24 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0025_alter_ordentrabajo_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='precio',
            new_name='precioTotal',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='usuario',
            new_name='vendedor',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='identificacion',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='telefonoCliente',
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='precioUnitario',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='venta',
            name='apellidoCliente',
            field=models.CharField(default='a'),
        ),
        migrations.AddField(
            model_name='venta',
            name='correo',
            field=models.CharField(default='example@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='venta',
            name='identificacion',
            field=models.IntegerField(default=1234567890),
        ),
        migrations.AddField(
            model_name='venta',
            name='nombreCliente',
            field=models.CharField(default='a'),
        ),
        migrations.AddField(
            model_name='venta',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.sucursal'),
        ),
        migrations.AddField(
            model_name='venta',
            name='telefonoCliente',
            field=models.PositiveBigIntegerField(default=1234567890),
        ),
        migrations.AlterField(
            model_name='ordentrabajo',
            name='jefeTaller',
            field=models.ForeignKey(blank=True, limit_choices_to={'rol__id': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.usuario'),
        ),
    ]
