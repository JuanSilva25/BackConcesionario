# Generated by Django 4.2.5 on 2023-11-19 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0045_cotizacion_permiso_cotizaciones'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permisorutas',
            options={},
        ),
        migrations.AddField(
            model_name='rutas',
            name='descripcion_Ruta',
            field=models.CharField(default='sin rutas', max_length=50),
        ),
        migrations.AlterField(
            model_name='rutas',
            name='nombreRuta',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='permisorutas',
            table=None,
        ),
    ]
