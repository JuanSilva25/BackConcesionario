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


@csrf_exempt
def login_view(request):
    print("La vista de inicio de sesión se ha llamado")  # Esta línea se imprimirá cada vez que se llame a la vista
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Intentando iniciar sesión con el usuario {username}")  # Esta línea se imprimirá cuando se haga una solicitud POST
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Inicio de sesión exitoso")  # Esta línea se imprimirá cuando el inicio de sesión sea exitoso
            return HttpResponse("Inicio de sesión exitoso")
        else:
            print("Credenciales inválidas")  # Esta línea se imprimirá cuando las credenciales sean inválidas
            return HttpResponse("Credenciales inválidas")
    else:
        print("Método no permitido")  # Esta línea se imprimirá cuando el método de la solicitud no sea POST
        return HttpResponse("Método no permitido")
