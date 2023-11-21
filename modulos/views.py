from rest_framework import viewsets
from .serializer import UsuarioSerializer,RolesSerializer,PermisoRutasSerializer,RutasSerializer,CategoriaRepuestoSerializer,RepuestoSerializer,OrdenTrabajoSerializer,InventarioVehiculoSerializer
from .serializer import InventarioRepuestoSerializer,CotizacionSerializer,VehiculoSerializer,SucursalSerializer,VentaSerializer,DetalleVentaSerializer
from .models import Usuario,Roles,PermisoRutas,Rutas,CategoriaRepuesto,Repuesto,OrdenTrabajo,InventarioVehiculo,InventarioRepuesto,Cotizacion,Sucursal,Vehiculo,Venta,DetalleVenta
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


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

class InvVehiculoView(viewsets.ModelViewSet):
     serializer_class = InventarioVehiculoSerializer
     queryset = InventarioVehiculo.objects.all()     

class InvRepuestoView(viewsets.ModelViewSet):
    serializer_class = InventarioRepuestoSerializer
    queryset = InventarioRepuesto.objects.all()     

class CotizacionView(viewsets.ModelViewSet):
    serializer_class = CotizacionSerializer
    queryset = Cotizacion.objects.all()  

class SucursalView(viewsets.ModelViewSet):
     serializer_class = SucursalSerializer
     queryset = Sucursal.objects.all()
     
     
class VehiculoView(viewsets.ModelViewSet):
     serializer_class = VehiculoSerializer
     queryset = Vehiculo.objects.all()


class VentaView(viewsets.ModelViewSet):
       serializer_class = VentaSerializer
       queryset = Venta.objects.all()




     
class DetalleVentaView(viewsets.ModelViewSet):
      serializer_class = DetalleVentaSerializer
      queryset = DetalleVenta.objects.all()
      
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
