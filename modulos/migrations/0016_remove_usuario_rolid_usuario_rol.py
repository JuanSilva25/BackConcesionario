# Generated by Django 4.2.6 on 2023-10-16 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0015_rename_rolid_roles_id_alter_usuario_idusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rolId',
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(blank=True, db_column='rol', null=True, on_delete=django.db.models.deletion.SET_NULL, to='modulos.roles'),
        ),
    ]