import datetime
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models import F,Q, Sum
from decimal import Decimal
from django.db import transaction


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
    nombreRuta = models.CharField(max_length=100)
    descripcion_Ruta =models.CharField(max_length = 50,default='sin rutas2')
  
     
    def __str__(self):
        return self.nombreRuta
     
    class Meta:
        db_table= 'Rutas'
        verbose_name_plural = 'Rutas'            
          
class PermisoRutas(models.Model):
    idPermiso = models.AutoField(primary_key=True)
    rolId = models.ForeignKey(Roles, on_delete=models.CASCADE)
    rutas = models.ManyToManyField(Rutas)

    def get_rutas(self):
        return ', '.join(str(ruta) for ruta in self.rutas.all())

    def __str__(self):
        return f"Permiso para {self.rolId} en rutas: {self.get_rutas()}"

    class Meta:
        db_table = 'permisoRutas'
        verbose_name_plural = 'permisoRutas'
    
class CategoriaRepuesto(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    tipoRepuesto = models.CharField(max_length=50, null=True, blank=True, default=None)

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
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"InventarioVehiculo {self.invVehiculoId} - Vehículo: {self.vehiculo}"
    
    class Meta:
        db_table = 'InventarioVehiculo'
        verbose_name_plural = 'InventarioVehiculo'

    def actualizar_inventario(self, cantidad_vendida):
        """
        Actualiza la cantidad de vehículos en el inventario después de una venta.
        """
        if cantidad_vendida > 0:
            try:
                with transaction.atomic():
                    inventario_existente = InventarioVehiculo.objects.select_for_update().filter(vehiculo=self.vehiculo).first()

                    if inventario_existente:
                        # Si existe, actualiza la cantidad existente
                        inventario_existente.cantidad += cantidad_vendida
                        inventario_existente.save()
                        print(f"Inventario actualizado - Vehículo: {self.vehiculo}, Nueva cantidad: {inventario_existente.cantidad}")
                    else:
                        # Si no existe, crea uno nuevo
                        InventarioVehiculo.objects.create(vehiculo=self.vehiculo, cantidad=cantidad_vendida)
                        print(f"Inventario creado - Vehículo: {self.vehiculo}, Cantidad: {cantidad_vendida}")

            except Exception as e:
                print(f"Error al actualizar inventario: {e}")

class Vehiculo(models.Model):
    vehiculoId= models.AutoField(primary_key =True)
    marca = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, null=True)
    precio = models.FloatField()
    img = models.URLField(max_length=300, default='sin imagen')
    color = models.CharField(max_length=100)
    modelo = models.IntegerField()
     
    def __str__(self):
        return f"{self.marca} {self.nombre} - Modelo {self.modelo}"
    
    class Meta:
        db_table ='Vehiculo'
        verbose_name_plural = 'Vehiculo'

class Repuesto(models.Model):
    repuestoId = models.AutoField(primary_key=True)
    nombreRepuesto = models.ForeignKey(CategoriaRepuesto, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    fechaFabriacion = models.CharField(default=datetime.date.today)
    img = models.URLField(max_length=300, default='sin imagen')  # Cambiado a URLField

    def __str__(self):
        return f'Repuesto {self.repuestoId} - Nombre: {self.nombreRepuesto}'

    class Meta:
        db_table = 'Repuesto'
        verbose_name_plural = 'Repuesto'


class InventarioRepuesto(models.Model):
    invRepuestolId = models.AutoField(primary_key=True)
    repuesto = models.ForeignKey('Repuesto', on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'InventarioRepuesto {self.invRepuestolId} - Repuesto: {self.repuesto}'

    class Meta:
        db_table = 'InventarioRepuesto'
        verbose_name_plural = 'InventarioRepuesto'

    def actualizar_inventario(self, cantidad_vendida):
        """
        Actualiza la cantidad de repuestos en el inventario después de una venta.
        """
        if cantidad_vendida > 0:
            self.cantidad -= cantidad_vendida
            self.save()

class Cotizacion(models.Model):
    cotizacionId = models.AutoField(primary_key =True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE,  null=True, limit_choices_to={'rol__id': 1})
    fecha = models.CharField(default=datetime.date.today)
    precio = models.FloatField()
    permiso_Cotizaciones= models.OneToOneField(PermisoRutas, on_delete=models.CASCADE, null=True, limit_choices_to={'idPermiso': 7})
    nombreCliente = models.CharField(default='a')
    apellidoCliente = models.CharField(default='a')
    identificacion = models.IntegerField(default=1234567890)

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
    ventaId = models.AutoField(primary_key=True)
    vendedor_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, limit_choices_to={'rol': 1})
    fecha = models.CharField(default=datetime.date.today)
    nombreCliente = models.CharField(default='a')
    apellidoCliente = models.CharField(default='a')
    identificacion = models.IntegerField(default=1234567890)
    telefonoCliente = models.PositiveBigIntegerField(default=1234567890)
    correo = models.CharField(max_length=100, default='example@gmail.com')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, limit_choices_to={})

    METODO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de crédito'),
        ('transferencia', 'Transferencia bancaria'),
        ('cheque', 'Cheque'),
    ]

    metodoPago = models.CharField(default='efectivo', choices=METODO_PAGO_CHOICES)
    precioTotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.0'), editable=False, blank=True)

    def __str__(self):
        return str(self.ventaId)  # Devuelve el número de venta como cadena

    class Meta:
        db_table = 'Venta'

    def save(self, *args, **kwargs):
        # Guardar el objeto antes de calcular los totales
        super().save(*args, **kwargs)

        # Actualizar el inventario de vehículos
        detalles_vehiculo = DetalleVenta.objects.filter(venta=self, vehiculo__isnull=False)
        for detalle_vehiculo in detalles_vehiculo:
            inventario_vehiculo = InventarioVehiculo.objects.get(vehiculo=detalle_vehiculo.vehiculo)
            inventario_vehiculo.actualizar_inventario(detalle_vehiculo.cantidad_vehiculo)

        # Actualizar el inventario de repuestos
        detalles_repuesto = DetalleVenta.objects.filter(venta=self, repuesto__isnull=False)
        for detalle_repuesto in detalles_repuesto:
            inventario_repuesto = InventarioRepuesto.objects.get(repuesto=detalle_repuesto.repuesto)
            inventario_repuesto.actualizar_inventario(detalle_repuesto.cantidad_repuesto)


class DetalleVenta(models.Model):
    detalleVentaId = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True, blank=True)
    repuesto = models.ForeignKey('Repuesto', on_delete=models.CASCADE, null=True, blank=True)
    cantidad_vehiculo = models.PositiveIntegerField(default=0)
    cantidad_repuesto = models.PositiveIntegerField(default=0)
    precio_unitario_vehiculo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False)
    precio_unitario_repuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False)
    total_vehiculo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False)
    total_repuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False)

    class Meta:
        db_table = 'DetalleVenta'

    def save(self, *args, **kwargs):
        if self.vehiculo:
            self.precio_unitario_vehiculo = self.vehiculo.precio
            self.total_vehiculo = self.cantidad_vehiculo * self.precio_unitario_vehiculo

        if self.repuesto:
            self.precio_unitario_repuesto = self.repuesto.precio
            self.total_repuesto = self.cantidad_repuesto * self.precio_unitario_repuesto

        # Guardar el objeto después de calcular los totales
        super().save(*args, **kwargs)

        # Actualizar el precioTotal de la venta después de guardar el detalle
        self.actualizar_precio_total_venta()

    def actualizar_precio_total_venta(self):
        # Calcular el precioTotal de la venta sumando los totales de detalles asociados
        precio_total_vehiculo = DetalleVenta.objects.filter(venta=self.venta, vehiculo__isnull=False).aggregate(Sum('total_vehiculo'))['total_vehiculo__sum'] or Decimal('0.00')
        precio_total_repuesto = DetalleVenta.objects.filter(venta=self.venta, repuesto__isnull=False).aggregate(Sum('total_repuesto'))['total_repuesto__sum'] or Decimal('0.00')

        # Actualizar el precioTotal de la venta
        self.venta.precioTotal = precio_total_vehiculo + precio_total_repuesto
        self.venta.save()

        # Actualizar el inventario de vehículos
        if self.vehiculo:
            inventario_vehiculo = InventarioVehiculo.objects.get(vehiculo=self.vehiculo)
            inventario_vehiculo.actualizar_inventario(self.cantidad_vehiculo)

        # Actualizar el inventario de repuestos
        if self.repuesto:
            inventario_repuesto = InventarioRepuesto.objects.get(repuesto=self.repuesto)
            inventario_repuesto.actualizar_inventario(self.cantidad_repuesto)