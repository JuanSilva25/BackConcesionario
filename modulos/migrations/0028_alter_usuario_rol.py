# Generated by Django 4.2.5 on 2023-11-05 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0027_alter_detalleventa_options_alter_cotizacion_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(blank=True, db_column='rol', null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.roles'),
        ),
    ]