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
      
     

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()

    def get_serializer_class(self):
        return DetalleVentaSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Asigna el valor del campo precio_unitario_vehiculo
        serializer.validated_data['precio_unitario_vehiculo'] = serializer.validated_data['vehiculo'].precio

        detalle_venta = DetalleVenta.objects.create(**serializer.validated_data)

        return Response(serializer.data)
    
class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()

    def get_serializer_class(self):
        return DetalleVentaSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Asigna el valor del campo precio_unitario_vehiculo
        serializer.validated_data['precio_unitario_vehiculo'] = serializer.validated_data['vehiculo'].precio

        detalle_venta = DetalleVenta.objects.create(**serializer.validated_data)

        return Response(serializer.data)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from django.db import IntegrityError
from django.contrib.sessions.models import Session

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            print(f"Usuario {username} no encontrado")
            return JsonResponse({'message': 'Credenciales inválidas'}, status=401)

        if user.password == password:
            # Almacena el ID de usuario en la sesión
            request.session['user_id'] = user.idUsuario

            print(f"Login exitoso para el usuario {username}")
            return JsonResponse({'message': 'Login exitoso'})
        else:
            print(f"Credenciales inválidas para el usuario {username}")
            return JsonResponse({'message': 'Credenciales inválidas'}, status=401)

    return JsonResponse({'message': 'Método no permitido'}, status=405)

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def get_user_details(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        
        if user_id:
            try:
                user = Usuario.objects.get(idUsuario=user_id)
                user_details = {
                    'id': user.idUsuario,
                    'username': user.username,
                    'nombre': user.nombre,
                    'apellido': user.apellido,
                    'email': user.email,
                    'telefono': user.telefono,
                    'direccion': user.direccion,
                    'rol': user.get_rol(),
                }
                print(f"Detalles del usuario: {user_details}")
                return JsonResponse({'user': user_details})
            except Usuario.DoesNotExist:
                print("Usuario no encontrado")
                return JsonResponse({'message': 'Usuario no encontrado'}, status=404)
        else:
            print("Usuario no autenticado")
            return JsonResponse({'message': 'Usuario no autenticado'}, status=401)
    else:
        print("Método no permitido")
        return JsonResponse({'message': 'Método no permitido'}, status=405)