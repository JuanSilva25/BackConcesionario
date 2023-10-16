# Generated by Django 4.2.6 on 2023-10-16 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0018_remove_ordentrabajo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rolId',
            field=models.ForeignKey(blank=True, db_column='rolId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.roles'),
        ),
    ]
