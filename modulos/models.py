
from django.db import models

class Roles(models.Model):
    rolId = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.rol

    class Meta:
        db_table = 'roles'
        verbose_name_plural = "roles"

class Usuario(models.Model):
    idUsuario = models.AutoField(Roles, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rolId = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, db_column='rolId')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'usuarios'
        verbose_name_plural = "usuarios"


class Rutas(models.Model):
     idRuta = models.AutoField(primary_key= True)
      
     
     def _str_(self):
         return self.idRuta
     
     class Meta:
          db_table= 'Rutas'
          verbose_name_plural = 'Rutas'
          
class PermisoRutas(models.Model):
    idPermiso = models.AutoField(primary_key=True)
    rolId = models.SmallIntegerField()
    
    
    def _str_(self):
        return self.rolId
    
    class Meta:
     db_table= 'permisoRutas'
     verbose_name_plural = 'permisoRutas'
     
          
          
class CategoriaRepuesto(models.Model):
      motor = models.CharField(max_length=100)
      transmision = models.CharField(max_length=100)
      suspension = models.CharField(max_length=100)
      llanta = models.CharField(max_length=100)
      carroceria = models.CharField(max_length=100)
      electrico = models.CharField(max_length=100)
      
      def __str__(self): 
          return self.id
      class Meta:
          db_table = 'CategoriaRepuesto'
          verbose_name_plural = 'CategoriaRepuestos'
          
class Repuesto(models.Model):
    repuestoId = models.AutoField(primary_key=True)
    nombreRepuesto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    unidades = models.PositiveIntegerField()  
    precio = models.FloatField()

    def __str__(self):
        return self.repuestoId

    class Meta:
        db_table = 'Repuesto'
        verbose_name_plural = 'Repuesto'

    
    
class OrdenTrabajo(models.Model):
        OrdenId= models.AutoField(primary_key =True)
        placa = models.CharField(max_length=100)
        nombreCliente = models.CharField(max_length=100)
        idUsuario = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True)
        telefonoCliente = models.PositiveIntegerField()
        correo= models.CharField(max_length=100)
        jefeTallerid= models.PositiveBigIntegerField()
        descripcion = models.CharField( max_length=100)
        fechainicio =models.CharField(max_length=100)
        fechaFinal = models.CharField(max_length=100)
        estado = models.CharField(max_length=50)
        
        def __str__(self):
         return self.OrdenId
        class Meta:
            db_table = 'OrdenTrabajo'
            verbose_name_plural = 'OrdenTrabajo'