from django.contrib import admin
from .models import Usuario,Roles,PermisoRutas,Rutas,CategoriaRepuesto,Repuesto,OrdenTrabajo,InventarioVehiculo,InventarioRepuesto,Cotizacion,Sucursal,Vehiculo,Venta,DetalleVenta
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Roles)
admin.site.register(PermisoRutas)
admin.site.register(CategoriaRepuesto)
admin.site.register(Repuesto)
admin.site.register(Rutas)
admin.site.register(OrdenTrabajo)
admin.site.register(InventarioVehiculo)
admin.site.register(InventarioRepuesto)
admin.site.register(Cotizacion)
admin.site.register(Sucursal)
admin.site.register(Vehiculo)
admin.site.register(Venta)
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(DetalleVenta)

