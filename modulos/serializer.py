from rest_framework import serializers
from .models import Usuario, Roles,PermisoRutas,Rutas, CategoriaRepuesto,Repuesto,OrdenTrabajo,InventarioVehiculo,InventarioRepuesto,Cotizacion
from .models import Sucursal,Vehiculo,Venta,DetalleVenta

class UsuarioSerializer(serializers.ModelSerializer):
    rol = serializers.SlugRelatedField(slug_field='rol', queryset=Roles.objects.all()) # Mostrar el nombre del 

    class Meta:
        model = Usuario
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class PermisoRutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoRutas
        fields  = ('idPermiso','rolId')
        
class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = ['idRuta']

class CategoriaRepuestoSerializer(serializers.ModelSerializer):
     class Meta:
         model = CategoriaRepuesto
         fields = '__all__'

class RepuestoSerializer(serializers.ModelSerializer):
      class Meta:
         model = Repuesto
         fields = '__all__'
         

class OrdenTrabajoSerializer(serializers.ModelSerializer):
      class Meta:
        model = OrdenTrabajo
        fields ='__all__'

class InventarioVehiculoSerializer(serializers.ModelSerializer):
      class Meta:
        model = InventarioVehiculo
        fields ='__all__'

class InventarioRepuestoSerializer(serializers.ModelSerializer):
      class Meta:
        model = InventarioRepuesto
        fields ='__all__'        

class CotizacionSerializer(serializers.ModelSerializer):
      class Meta:
        model = Cotizacion
        fields ='__all__'        


class SucursalSerializer(serializers.ModelSerializer):
      class Meta:
        model= Sucursal
        fields = '__all__'
      
class VehiculoSerializer(serializers.ModelSerializer):
      class Meta:
        model= Vehiculo
        fields = '__all__'
     
class VentaSerializer(serializers.ModelSerializer):
      class Meta:
        model= Venta
        fields = '__all__'
        
class DetalleVentaSerializer(serializers.ModelSerializer):
      class Meta:
        model= DetalleVenta
        fields = '__all__'
