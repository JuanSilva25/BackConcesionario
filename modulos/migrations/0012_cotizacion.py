# Generated by Django 4.2.6 on 2023-10-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0011_inventariorepuesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('cotizacionId', models.AutoField(primary_key=True, serialize=False)),
                ('vehiculoId', models.PositiveIntegerField()),
                ('usuarioId', models.PositiveIntegerField()),
                ('fecha', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Cotizacion',
                'db_table': 'Cotizacion',
            },
        ),
    ]