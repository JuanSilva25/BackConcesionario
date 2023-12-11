# Generated by Django 4.2.5 on 2023-12-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0066_alter_venta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('en proceso', 'En proceso'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado'), ('cotizacion', 'Cotizacion')], default='En proceso', max_length=50),
        ),
    ]