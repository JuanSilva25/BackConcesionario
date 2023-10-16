from rest_framework import serializers
from .models import Usuario, Roles,PermisoRutas,Rutas, CategoriaRepuesto,Repuesto,OrdenTrabajo

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #fields = ('idUsuario','username','password','nombre','apellido','rolId')
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