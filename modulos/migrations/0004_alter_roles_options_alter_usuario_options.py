# Generated by Django 4.2.6 on 2023-10-14 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_alter_roles_table_alter_usuario_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name_plural': 'roles'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'usuarios'},
        ),
    ]
