from rest_framework import serializers
from .models import Usuario, Roles,PermisoRutas,Rutas, CategoriaRepuesto,Repuesto,OrdenTrabajo,InventarioVehiculo,InventarioRepuesto,Cotizacion
from .models import Sucursal,Vehiculo,Venta,DetalleVenta
from rest_framework import viewsets
from rest_framework.response import Response
from .models import PermisoRutas, Rutas

class UsuarioSerializer(serializers.ModelSerializer):
    rol_name = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = '__all__'

    def get_rol_name(self, instance):
        if instance.rol:
            return instance.rol.rol
        return "Sin Rol"
    
    



class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class PermisoRutasSerializer(serializers.ModelSerializer):
    ruta_names = serializers.SerializerMethodField()

    class Meta:
        model = PermisoRutas
        fields = ('idPermiso', 'rolId', 'rutas', 'ruta_names')

    def get_ruta_names(self, instance):
        return [ruta.nombreRuta for ruta in instance.rutas.all()] if instance.rutas.exists() else ["Sin Ruta"]
    def retrieve(self, request, rol_id=None):
        permiso_rutas = PermisoRutas.objects.get(rolId=rol_id)
        rutas = permiso_rutas.rutas.all()
        serializer = RutasSerializer(rutas, many=True)
        return Response({
            'permiso_rutas': permiso_rutas.idPermiso,
            'rutas': serializer.data
        })
        
class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = '__all__'    
        

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
        
        
  