from rest_framework import serializers
from .models import Usuario, Roles

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #fields = ('idUsuario','username','password','nombre','apellido','rolId')
        fields = '__all__'

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'