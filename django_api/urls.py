"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('modulos.urls')),
    path('roles/', include('modulos.urls')),
    path('permisoruta/', include('modulos.urls')),
    path('rutas/', include('modulos.urls')),
    path('categoriarespuesto/', include('modulos.urls')),
    path('repuesto/', include('modulos.urls')),
    path('ordentrabajo/', include('modulos.urls')),
    path('inventariovehiculo/', include('modulos.urls')),
    path('cotizacion/', include('modulos.urls')),
    path('sucursal/',include('modulos.urls')),
    path('vehiculo/',include('modulos.urls')),
    path('venta/',include('modulos.urls')),
    path('detalleventa/',include('modulos.urls')),
    path('login/', include('modulos.urls')),
    path('api/', include('modulos.urls')), 
]