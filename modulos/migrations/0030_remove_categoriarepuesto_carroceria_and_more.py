# Generated by Django 4.2.6 on 2023-10-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0029_categoriarepuesto_tiporepuesto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriarepuesto',
            name='carroceria',
        ),
        migrations.RemoveField(
            model_name='categoriarepuesto',
            name='electrico',
        ),
        migrations.RemoveField(
            model_name='categoriarepuesto',
            name='llanta',
        ),
        migrations.RemoveField(
            model_name='categoriarepuesto',
            name='motor',
        ),
        migrations.RemoveField(
            model_name='categoriarepuesto',
            name='suspension',
        ),
        migrations.RemoveField(
            model_name='categoriarepuesto',
            name='transmision',
        ),
        migrations.AlterField(
            model_name='categoriarepuesto',
            name='tipoRepuesto',
            field=models.CharField(max_length=50),
        ),
    ]