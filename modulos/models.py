import datetime
from django.db import models


class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.rol

    class Meta:
        db_table = 'roles'
        verbose_name_plural = "roles"

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(default="example@example.com")
    telefono = models.IntegerField(default=1234567890)
    direccion = models.CharField(default='Sin dirección')
    rolId = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, db_column='rolId')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'usuarios'
        verbose_name_plural = "usuarios"

          
class PermisoRutas(models.Model):
    idPermiso = models.AutoField(primary_key=True)
    rolId = models.ForeignKey(Roles, on_delete=models.CASCADE)  # Relación ForeignKey a la tabla Roles
    
    def __str__(self):
        return str(self.rolId.id)  # Puedes acceder al ID del rol relacionado
    
    class Meta:
     db_table= 'permisoRutas'
     verbose_name_plural = 'permisoRutas'
            

class Rutas(models.Model):
    idRuta = models.AutoField(primary_key= True)
    nombreRuta = models.CharField(default='Sin nombre')
     
    def _str_(self):
        return self.nombreRuta
     
    class Meta:
        db_table= 'Rutas'
        verbose_name_plural = 'Rutas'            
          
class CategoriaRepuesto(models.Model):
    tipoRepuesto = models.CharField(max_length=50, null=True)
    motor = models.CharField(max_length=100, null=True)
    transmision = models.CharField(max_length=100, null=True)
    suspension = models.CharField(max_length=100, null=True)
    llanta = models.CharField(max_length=100, null=True)
    carroceria = models.CharField(max_length=100, null=True)
    electrico = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tipoRepuesto

    class Meta:
        db_table = 'CategoriaRepuesto'
        verbose_name_plural = 'CategoriaRepuestos'

          
class Repuesto(models.Model):
    repuestoId = models.AutoField(primary_key=True)
    nombreRepuesto = models.ForeignKey(CategoriaRepuesto, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    unidades = models.PositiveIntegerField()
    precio = models.FloatField()
    fechaFabriacion = models.CharField(default=datetime.date.today)

    def __str__(self):
        return f'Repuesto {self.repuestoId} - Nombre: {self.nombreRepuesto}, Unidades: {self.unidades}'

    class Meta:
        db_table = 'Repuesto'
        verbose_name_plural = 'Repuesto'


    
    
class OrdenTrabajo(models.Model):
    OrdenId= models.AutoField(primary_key =True)
    jefeTaller = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    placa = models.CharField(max_length=100)
    nombreCliente = models.CharField(max_length=100)
    telefonoCliente = models.PositiveIntegerField()
    correo= models.CharField(max_length=100)
    descripcion = models.CharField( max_length=100)
    fechainicio =models.CharField(max_length=100)
    fechaFinal = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    precioTotal = models.FloatField(default=0.0)
        
    def __str__(self):
        return self.OrdenId
    class Meta:
        db_table = 'OrdenTrabajo'
        verbose_name_plural = 'OrdenTrabajo'


class InventarioVehiculo(models.Model):
    invVehiculoId = models.AutoField(primary_key =True)
    vehiculoId = models.PositiveIntegerField() #cambiar
    sucursalId = models.PositiveIntegerField() #cambiar
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.invVehiculoId
    class Meta:
        db_table = 'InvetarioVehiculo'
        verbose_name_plural = 'InventarioVehiculo'


class InventarioRepuesto(models.Model):
    invRepuestolId = models.AutoField(primary_key=True)
    repuesto = models.ForeignKey('Repuesto', on_delete=models.CASCADE, null=True)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'InventarioRepuesto {self.invRepuestolId} - Repuesto: {self.repuesto}, Sucursal: {self.sucursal}, Cantidad: {self.cantidad}'

    class Meta:
        db_table = 'InventarioRepuesto'
        verbose_name_plural = 'InventarioRepuesto'


class Cotizacion(models.Model):
    cotizacionId = models.AutoField(primary_key =True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE,  null=True)
    fecha = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return f"Cotización {self.cotizacionId} - Vehículo: {self.vehiculo}, Usuario: {self.usuario}"
    
    class Meta:
        db_table = 'Cotizacion'
        verbose_name_plural = 'Cotizacion'

class Sucursal(models.Model):
    sucursalId= models.AutoField(primary_key =True)
    nombre = models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    telefono= models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)        
          
    def __str__(self):
        return self. sucursalId
    class Meta:
        db_table = 'Sucursal'
        verbose_name_plural= 'Sucursal'
                            
class Vehiculo(models.Model):
    vehiculoId= models.AutoField(primary_key =True)
    marca = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, null=True)
    precio = models.FloatField()
    img = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    modelo = models.IntegerField()
     
    def __str__(self):
        return f"{self.marca} {self.nombre} - Modelo {self.modelo}"
    
    class Meta:
        db_table ='Vehiculo'
        verbose_name_plural = 'Vehiculo'
             
class Venta(models.Model):
    ventaId= models.AutoField(primary_key =True)
    usuario = usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE,  null=True)
    telefonoCliente = models.PositiveBigIntegerField()
    correo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    precio = models.FloatField()
      
    def __str__(self):
       return str(self.ventaId)  # Devuelve el número de venta como cadena
    
    class Meta:
        db_table ='Venta'
        verbose_name_plural = 'Venta'
        
        
class DetalleVenta(models.Model):
    detalleVentaId= models.AutoField(primary_key =True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)  # Clave externa que relaciona DetalleVenta con Venta
    cantidad= models.PositiveIntegerField()
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True)
    subtotal = models.FloatField()
     
    def __str__(self):
       return str(self.detalleVentaId)  # Devuelve el ID del detalle de venta como cadena
    class Meta:
        db_table ='DetalleVenta'
        verbose_name_plural ='DetalleVenta'