# Generated by Django 4.2.6 on 2023-10-14 23:12

from django.db import migrations, models
import modulos.models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_usuario_esgerente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='esGerente',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=modulos.models.Roles),
        ),
    ]
