from rest_framework import viewsets
from .serializer import UsuarioSerializer,RolesSerializer,PermisoRutasSerializer,RutasSerializer,CategoriaRepuestoSerializer,RepuestoSerializer,OrdenTrabajoSerializer,InventarioVehiculoSerializer
from .serializer import InventarioRepuestoSerializer,CotizacionSerializer,VehiculoSerializer,SucursalSerializer,VentaSerializer,DetalleVentaSerializer
from .models import Usuario,Roles,PermisoRutas,Rutas,CategoriaRepuesto,Repuesto,OrdenTrabajo,InventarioVehiculo,InventarioRepuesto,Cotizacion,Sucursal,Vehiculo,Venta,DetalleVenta
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
     
@api_view(['GET'])
def lista_inventario_vehiculos(request):
    inventario_vehiculos = InventarioVehiculo.objects.all()
    serializer = InventarioVehiculoSerializer(inventario_vehiculos, many=True)
    return Response(serializer.data)
     
class VentaView(viewsets.ModelViewSet):
      serializer_class = VentaSerializer
      queryset = Venta.objects.all()
      
     
class DetalleVentaView(viewsets.ModelViewSet):
      serializer_class = DetalleVentaSerializer
      queryset = DetalleVenta.objects.all()

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Usuario

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario utilizando el nuevo backend
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user)

            # Puedes devolver cualquier información adicional que desees en el JSON de respuesta
            return JsonResponse({'message': 'Login exitoso'})
        else:
            return JsonResponse({'message': 'Credenciales inválidas'}, status=401)

    return JsonResponse({'message': 'Método no permitido'}, status=405)
