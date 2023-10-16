# Generated by Django 4.2.6 on 2023-10-16 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0016_remove_usuario_rolid_usuario_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='idUsuario',
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.usuario'),
        ),
    ]
