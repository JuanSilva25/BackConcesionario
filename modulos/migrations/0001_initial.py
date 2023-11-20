# Generated by Django 4.2.6 on 2023-11-20 03:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaRepuesto',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('tipoRepuesto', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'CategoriaRepuestos',
                'db_table': 'CategoriaRepuesto',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'roles',
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('idRuta', models.AutoField(primary_key=True, serialize=False)),
                ('nombreRuta', models.CharField(max_length=100)),
                ('descripcion_Ruta', models.CharField(default='sin rutas2', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Rutas',
                'db_table': 'Rutas',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('sucursalId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField()),
                ('ciudad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sucursal',
                'db_table': 'Sucursal',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.CharField(default='example@example.com')),
                ('telefono', models.IntegerField(default=1234567890)),
                ('direccion', models.CharField(default='Sin dirección')),
                ('rol', models.ForeignKey(blank=True, db_column='rol', null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.roles')),
            ],
            options={
                'verbose_name_plural': 'usuarios',
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('vehiculoId', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('precio', models.FloatField()),
                ('img', models.URLField(default='sin imagen', max_length=300)),
                ('color', models.CharField(max_length=100)),
                ('modelo', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Vehiculo',
                'db_table': 'Vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('ventaId', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(default=datetime.date.today)),
                ('nombreCliente', models.CharField(default='a')),
                ('apellidoCliente', models.CharField(default='a')),
                ('identificacion', models.IntegerField(default=1234567890)),
                ('telefonoCliente', models.PositiveBigIntegerField(default=1234567890)),
                ('correo', models.CharField(default='example@gmail.com', max_length=100)),
                ('metodoPago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de crédito'), ('transferencia', 'Transferencia bancaria'), ('cheque', 'Cheque')], default='efectivo')),
                ('precioTotal', models.FloatField(blank=True, default=0.0, editable=False)),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.sucursal')),
                ('vendedor_id', models.ForeignKey(limit_choices_to={'rol': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.usuario')),
            ],
            options={
                'db_table': 'Venta',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('repuestoId', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('fechaFabriacion', models.CharField(default=datetime.date.today)),
                ('img', models.URLField(default='sin imagen', max_length=300)),
                ('nombreRepuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.categoriarepuesto')),
            ],
            options={
                'verbose_name_plural': 'Repuesto',
                'db_table': 'Repuesto',
            },
        ),
        migrations.CreateModel(
            name='PermisoRutas',
            fields=[
                ('idPermiso', models.AutoField(primary_key=True, serialize=False)),
                ('rolId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.roles')),
                ('rutas', models.ManyToManyField(to='modulos.rutas')),
            ],
            options={
                'verbose_name_plural': 'permisoRutas',
                'db_table': 'permisoRutas',
            },
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('OrdenId', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=100)),
                ('nombreCliente', models.CharField(max_length=100)),
                ('telefonoCliente', models.PositiveIntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fechainicio', models.CharField(default=datetime.date.today)),
                ('fechaFinal', models.CharField(default=datetime.date.today)),
                ('estado', models.CharField(choices=[('recibida', 'Recibida'), ('en proceso', 'En proceso'), ('finalizado', 'Finalizado')], max_length=50)),
                ('precioTotal', models.FloatField(default=0.0)),
                ('jefeTaller', models.ForeignKey(blank=True, limit_choices_to={'rol__id': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.usuario')),
            ],
            options={
                'verbose_name_plural': 'OrdenTrabajo',
                'db_table': 'OrdenTrabajo',
            },
        ),
        migrations.CreateModel(
            name='InventarioVehiculo',
            fields=[
                ('invVehiculoId', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('vehiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.vehiculo')),
            ],
            options={
                'verbose_name_plural': 'InventarioVehiculo',
                'db_table': 'InventarioVehiculo',
            },
        ),
        migrations.CreateModel(
            name='InventarioRepuesto',
            fields=[
                ('invRepuestolId', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('repuesto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.repuesto')),
            ],
            options={
                'verbose_name_plural': 'InventarioRepuesto',
                'db_table': 'InventarioRepuesto',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('detalleVentaId', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_vehiculo', models.PositiveIntegerField(default=0)),
                ('cantidad_repuesto', models.PositiveIntegerField(default=0)),
                ('total_vehiculo', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('total_repuesto', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('repuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.repuesto')),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.vehiculo')),
                ('venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.venta')),
            ],
            options={
                'verbose_name_plural': 'DetalleVenta',
                'db_table': 'DetalleVenta',
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('cotizacionId', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(default=datetime.date.today)),
                ('precio', models.FloatField()),
                ('nombreCliente', models.CharField(default='a')),
                ('apellidoCliente', models.CharField(default='a')),
                ('identificacion', models.IntegerField(default=1234567890)),
                ('permiso_Cotizaciones', models.OneToOneField(limit_choices_to={'idPermiso': 7}, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.permisorutas')),
                ('usuario', models.ForeignKey(limit_choices_to={'rol__id': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.usuario')),
                ('vehiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.vehiculo')),
            ],
            options={
                'verbose_name_plural': 'Cotizacion',
                'db_table': 'Cotizacion',
            },
        ),
    ]
