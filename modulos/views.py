from rest_framework import viewsets
from .serializer import UsuarioSerializer,RolesSerializer,PermisoRutasSerializer,RutasSerializer,CategoriaRepuestoSerializer,RepuestoSerializer,OrdenTrabajoSerializer
from .models import Usuario,Roles,PermisoRutas,Rutas,CategoriaRepuesto,Repuesto,OrdenTrabajo

# Create your views here.
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class RolesView(viewsets.ModelViewSet):
    serializer_class = RolesSerializer
    queryset = Roles.objects.all()

class PermisoRutasView(viewsets.ModelViewSet):
    serializer_class = PermisoRutasSerializer
    queryset = PermisoRutas.objects.all()
    
       
class RutasView(viewsets.ModelViewSet):
    serializer_class = RutasSerializer
    queryset = Rutas.objects.all()
    
class CategoriaRepuestoView(viewsets.ModelViewSet):
     serializer_class = CategoriaRepuestoSerializer
     queryset = CategoriaRepuesto.objects.all()
     
     
class RepuestoView(viewsets.ModelViewSet):
    serializer_class = RepuestoSerializer
    queryset = Repuesto.objects.all()
    

class OrdenTrabajoView(viewsets.ModelViewSet):
     serializer_class = OrdenTrabajoSerializer
     queryset = OrdenTrabajo.objects.all()