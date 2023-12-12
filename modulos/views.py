from django.db.models import Count, Sum
from .serializer import OrdenTrabajoSerializer
from .models import OrdenTrabajo
from rest_framework import request
from .serializer import VentaSerializer
from .models import OrdenTrabajo, DetalleVenta, Venta
from rest_framework.response import Response
from rest_framework.views import APIView
# Asegúrate de tener un serializador para el modelo Usuario
from .serializer import UsuarioSerializer
from django.db import IntegrityError
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import UsuarioSerializer, RolesSerializer, PermisoRutasSerializer, RutasSerializer, CategoriaRepuestoSerializer, RepuestoSerializer, OrdenTrabajoSerializer, InventarioVehiculoSerializer
from .serializer import InventarioRepuestoSerializer, CotizacionSerializer, VehiculoSerializer, SucursalSerializer, VentaSerializer, DetalleVentaSerializer
from .models import Usuario, Roles, PermisoRutas, Rutas, CategoriaRepuesto, Repuesto, OrdenTrabajo, InventarioVehiculo, InventarioRepuesto, Cotizacion, Sucursal, Vehiculo, Venta, DetalleVenta


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


class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()


class DetalleVentaView(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSerializer
    queryset = DetalleVenta.objects.all()


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Intenta obtener al usuario a través del nombre de usuario
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return JsonResponse({'message': 'Credenciales inválidas'}, status=401)

        # Verifica la contraseña
        if user.password == password:
            # Iniciar sesión
            # Aquí puedes realizar acciones adicionales antes de iniciar sesión si es necesario
            # Serializa los datos del usuario
            user_data = UsuarioSerializer(user).data
            # Incluye los datos del usuario en la respuesta
            return JsonResponse({'message': 'Login exitoso', 'user': user_data})
        else:
            return JsonResponse({'message': 'Credenciales inválidas'}, status=401)

    elif request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        return JsonResponse({'username': username, 'password': password})

    return JsonResponse({'message': 'Método no permitido'}, status=405)


class TotalesView(APIView):
    def get(self, request):
        # Totales para OrdenTrabajo
        total_ordenes = OrdenTrabajo.objects.count()
        total_vehiculos = DetalleVenta.objects.filter(
            vehiculo__isnull=False).count()
        total_repuestos = DetalleVenta.objects.filter(
            repuesto__isnull=False).count()
        total_precios = OrdenTrabajo.objects.aggregate(
            total=Sum('precioTotal'))['total'] or 0

        # Totales para DetalleVenta
        total_ventas_vehiculos = DetalleVenta.objects.filter(
            vehiculo__isnull=False).aggregate(total=Sum('total_vehiculo'))['total'] or 0
        total_ventas_repuestos = DetalleVenta.objects.filter(
            repuesto__isnull=False).aggregate(total=Sum('total_repuesto'))['total'] or 0
        total_ventas_general = total_ventas_vehiculos + total_ventas_repuestos

        cantidad_ventas_vehiculos = DetalleVenta.objects.filter(
            vehiculo__isnull=False).aggregate(cantidad=Sum('cantidad_vehiculo'))['cantidad'] or 0
        cantidad_ventas_repuestos = DetalleVenta.objects.filter(
            repuesto__isnull=False).aggregate(cantidad=Sum('cantidad_repuesto'))['cantidad'] or 0
        cantidad_ventas_general = total_ordenes + total_repuestos + total_vehiculos

        # Últimas 10 ventas
        ultimas_ventas = Venta.objects.order_by('-fecha')[:10]
        serializer = VentaSerializer(ultimas_ventas, many=True)

        return Response({
            'total_ordenes': total_ordenes,
            'total_precios_ordenes': total_precios,
            'total_ventas_vehiculos': total_ventas_vehiculos,
            'total_ventas_repuestos': total_ventas_repuestos,
            'total_ventas_general': total_ventas_general,
            'cantidad_ventas_vehiculos': cantidad_ventas_vehiculos,
            'cantidad_ventas_repuestos': cantidad_ventas_repuestos,
            'ultimas_ventas': serializer.data,
        })


class OrdenesClienteView(APIView):
    def post(self, request):
        placa = request.data.get('placa', None)
        identificacion = request.data.get('identificacion', None)

        if placa is not None:
            # Filtrar OrdenTrabajo basándose en la placa
            ordenes = OrdenTrabajo.objects.filter(placa=placa)
        elif identificacion is not None:
            # Filtrar OrdenTrabajo basándose en el número de identificación
            ordenes = OrdenTrabajo.objects.filter(
                identificacion_Cliente=identificacion)
        else:
            ordenes = OrdenTrabajo.objects.all()

        # Serializar las órdenes
        ordenes_serializer = OrdenTrabajoSerializer(ordenes, many=True)

        return Response({
            'ordenes': ordenes_serializer.data,
        })
