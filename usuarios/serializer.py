from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #fields = ('idUsuario','username','password','nombre','apellido','rolId')
        fields = '__all__'
