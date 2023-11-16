import datetime
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

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
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, db_column='rol')

    def __str__(self):
        return self.rol.rol
    
    def get_rol(self):
        if self.rol:
            return self.rol.rol
        return "Sin Rol"  # Otra opción si el rol es nulo.
    
    class Meta:
        db_table = 'usuarios'
        verbose_name_plural = "usuarios"


class Rutas(models.Model):
    idRuta = models.AutoField(primary_key= True)
    nombreRuta = models.CharField(default='Sin nombre')
  
     
    def __str__(self):
        return self.nombreRuta
     
    class Meta:
        db_table= 'Rutas'
        verbose_name_plural = 'Rutas'            
          
class PermisoRutas(models.Model):
    idPermiso = models.AutoField(primary_key=True)
    rolId = models.ForeignKey(Roles, on_delete=models.CASCADE)  # Relación ForeignKey a la tabla Roles
    rutas = models.ManyToManyField(Rutas)  # Relación ManyToManyField a la tabla Rutas

    def __str__(self):
        return f"Permiso para {self.rolId} en rutas: {', '.join(str(ruta) for ruta in self.rutas.all())}"

    class Meta:
        db_table = 'permisoRutas'
        verbose_name_plural = 'permisoRutas'


class CategoriaRepuesto(models.Model):
    tipoRepuesto = models.CharField(max_length=50, null=True)
    
    def __str__(self): 
        return self.tipoRepuesto
    
    class Meta:
        db_table = 'CategoriaRepuesto'
        verbose_name_plural = 'CategoriaRepuestos'
    
    
class OrdenTrabajo(models.Model):
    OrdenId= models.AutoField(primary_key =True)
    jefeTaller = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True,limit_choices_to={'rol__id': 2})
    placa = models.CharField(max_length=100)
    nombreCliente = models.CharField(max_length=100)
    telefonoCliente = models.PositiveIntegerField()
    correo= models.CharField(max_length=100)
    descripcion = models.CharField( max_length=100)
    fechainicio = models.CharField(default=datetime.date.today)
    fechaFinal = models.CharField(default=datetime.date.today)

    ESTADOS = [
        ('recibida', 'Recibida'),
        ('en proceso', 'En proceso'),
        ('finalizado', 'Finalizado'),
    ]

    estado = models.CharField(max_length=50, choices=ESTADOS)
    precioTotal = models.FloatField(default=0.0)
        
    def __str__(self):
        return self.nombreCliente
    class Meta:
        db_table = 'OrdenTrabajo'
        verbose_name_plural = 'OrdenTrabajo'


class InventarioVehiculo(models.Model):
    invVehiculoId = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"InventarioVehiculo {self.invVehiculoId} - Vehículo: {self.vehiculo}"
    
    class Meta:
        db_table = 'InventarioVehiculo'
        verbose_name_plural = 'InventarioVehiculo'

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

@receiver(post_save, sender=Vehiculo)
def agregar_vehiculo_a_inventario(sender, instance, created, **kwargs):
    if created:
        InventarioVehiculo.objects.create(vehiculo=instance)
  
@receiver(post_delete, sender=Vehiculo)
def eliminar_vehiculo_de_inventario(sender, instance, **kwargs):
    try:
        inventario_vehiculo = InventarioVehiculo.objects.get(vehiculo=instance)
        inventario_vehiculo.delete()
    except InventarioVehiculo.DoesNotExist:
        pass


class InventarioRepuesto(models.Model):
    invRepuestolId = models.AutoField(primary_key=True)
    repuesto = models.ForeignKey('Repuesto', on_delete=models.CASCADE, null=True)
  

    def __str__(self):
        return f'InventarioRepuesto {self.invRepuestolId} - Repuesto: {self.repuesto}'

    class Meta:
        db_table = 'InventarioRepuesto'
        verbose_name_plural = 'InventarioRepuesto'

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

@receiver(post_save, sender=Repuesto)
def agregar_repuesto_a_inventario(sender, instance, created, **kwargs):
    if created:
        InventarioRepuesto.objects.create(repuesto=instance)
  
@receiver(post_delete, sender=Repuesto)
def eliminar_repuesto_de_inventario(sender, instance, **kwargs):
    try:
        inventario_repuesto = InventarioRepuesto.objects.get(repuesto=instance)
        inventario_repuesto.delete()
    except InventarioRepuesto.DoesNotExist:
        pass

class Cotizacion(models.Model):
    cotizacionId = models.AutoField(primary_key =True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE,  null=True, limit_choices_to={'rol__id': 1})
    fecha = models.CharField(default=datetime.date.today)
    precio = models.FloatField()
    permiso_Cotizaciones= models.OneToOneField(PermisoRutas, on_delete=models.CASCADE, null=True, limit_choices_to={'idPermiso': 7})

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
        return self. nombre
    class Meta:
        db_table = 'Sucursal'
        verbose_name_plural= 'Sucursal'
                            
             
class Venta(models.Model):
    ventaId= models.AutoField(primary_key =True)
    vendedor_id = models.ForeignKey('Usuario', on_delete=models.CASCADE,  null=True,limit_choices_to={'rol': 1})
    fecha = models.CharField(default=datetime.date.today)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True,limit_choices_to={})
    nombreCliente = models.CharField(default= 'a')
    apellidoCliente = models.CharField(default= 'a')
    identificacion =  models.IntegerField(default= 1234567890)
    telefonoCliente = models.PositiveBigIntegerField(default= 1234567890)
    correo = models.CharField(max_length=100, default='example@gmail.com')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True,limit_choices_to={})
  
    METODO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de crédito'),
        ('transferencia', 'Transferencia bancaria'),
        ('cheque', 'Cheque'),
    ]

    metodoPago = models.CharField(default='efectivo' ,choices= METODO_PAGO_CHOICES)
    precioTotal = models.FloatField(default=0.0 ,editable=False, blank=True)

    permiso_Ventas= models.OneToOneField(PermisoRutas, on_delete=models.CASCADE, null=True, limit_choices_to={'idPermiso': 7})
    
   
    def __str__(self):
       return str(self.ventaId)  # Devuelve el número de venta como cadena
    
    class Meta:
        db_table ='Venta'


        
class DetalleVenta(models.Model):
    detalleVentaId = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField()
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.precioUnitario:
            # Calcular el precioUnitario basado en el vehículo seleccionado
            if self.venta and self.venta.vehiculo:
                self.precioUnitario = self.venta.vehiculo.precio
            else:
                self.precioUnitario = 0.0  # Puedes configurar otro valor predeterminado

        # Calcular el total en función de la cantidad y el precioUnitario
        self.total = self.cantidad * self.precioUnitario
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.detalleVentaId)
    
@receiver(post_save, sender=DetalleVenta)
def actualizar_precio_total_venta(sender, instance, **kwargs):
    # Obtén la venta asociada al detalle
    venta = instance.venta
    
    # Calcula el precioTotal como la suma de los totales de todos los detalles de la venta
    precio_total = sum(detalle.total for detalle in venta.detalleventa_set.all())
    
    # Actualiza el precioTotal de la venta
    venta.precioTotal = precio_total
    venta.save()    
