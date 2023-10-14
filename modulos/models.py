
# from django.db import models

# class Roles(models.Model):
#     rolId = models.AutoField(primary_key=True)
#     rol = models.CharField(max_length=50)

#     def __str__(self):
#         return self.rol

#     class Meta:
#         db_table = 'roles'
#         verbose_name_plural = "roles"

# class Usuario(models.Model):
#     idUsuario = models.AutoField(Roles, primary_key=True)
#     username = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     nombre = models.CharField(max_length=200)
#     apellido = models.CharField(max_length=200)
#     esGerente = models.BooleanField(default=False)
#     rolId = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = 'usuarios'
#         verbose_name_plural = "usuarios"

from django.db import models

class Roles(models.Model):
    rolId = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)
    usuarios = models.ManyToManyField('Usuario', related_name='roles')

    def __str__(self):
        return self.rol

    class Meta:
        db_table = 'roles'
        verbose_name_plural = 'roles'

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    esGerente = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'usuarios'
        verbose_name_plural = 'usuarios'
