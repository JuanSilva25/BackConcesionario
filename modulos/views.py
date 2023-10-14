from rest_framework import viewsets
from .serializer import UsuarioSerializer,RolesSerializer
from .models import Usuario,Roles

# Create your views here.
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class RolesView(viewsets.ModelViewSet):
    serializer_class = RolesSerializer
    queryset = Roles.objects.all()
