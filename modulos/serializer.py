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
        
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rolId'] = RolesSerializer(instance.rolId).data
        return representation
        
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
         
      def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['nombreRepuesto'] = CategoriaRepuestoSerializer(instance.nombreRepuesto).data
        return representation
         
class OrdenTrabajoSerializer(serializers.ModelSerializer):
    #jefeTaller = UsuarioSerializer(read_only=True)

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['jefeTaller'] = UsuarioSerializer(instance.jefeTaller).data
        return representation

class InventarioVehiculoSerializer(serializers.ModelSerializer):
      class Meta:
        model = InventarioVehiculo
        fields ='__all__'
        
      def to_representation(sel,instance):
          representation = super(). to_representation(instance)
          representation ['vehiculo'] = VehiculoSerializer(instance.vehiculo).data
          return representation
        
class InventarioRepuestoSerializer(serializers.ModelSerializer):
      class Meta:
        model = InventarioRepuesto
        fields ='__all__'        
        
      def to_representation(sel,instance):
          representation = super(). to_representation(instance)
          representation ['repuesto'] = RepuestoSerializer(instance.repuesto).data
          return representation  

class CotizacionSerializer(serializers.ModelSerializer):
      class Meta:
        model = Cotizacion
        fields ='__all__'        

      def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['vehiculo'] = VehiculoSerializer(instance.vehiculo).data
        representation['usuario'] = UsuarioSerializer(instance.usuario).data
        return representation

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
        model = Venta
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['vendedor_id'] = UsuarioSerializer(instance.vendedor_id).data
        representation['sucursal'] = SucursalSerializer(instance.sucursal).data
        representation['detalleventa_set'] = DetalleVentaSerializer(instance.detalleventa_set.all(), many=True).data
        return representation
   

class DetalleVentaSerializer(serializers.ModelSerializer):
    #vehiculo = VehiculoSerializer(read_only=True)
    #repuesto = RepuestoSerializer(read_only=True)

    class Meta:
        model = DetalleVenta
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['vehiculo'] = VehiculoSerializer(instance.vehiculo).data
        representation['repuesto'] = RepuestoSerializer(instance.repuesto).data
   
        return representation