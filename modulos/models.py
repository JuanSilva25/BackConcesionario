from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)  # Campo de identificación automática
    username = models.CharField(max_length=100, unique=True)  # Nombre de usuario único
    password = models.CharField(max_length=100)  # Contraseña
    nombre = models.CharField(max_length=200)  # Nombre del usuario
    apellido = models.CharField(max_length=200)  # Apellido del usuario
    rolId = models.IntegerField(null=True, blank=True) # Relación con el modelo de Rol
    
    def __str__(self):
        return self.username