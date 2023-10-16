from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from modulos import views

#api versioning
router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioView, 'usuario')
router.register(r'roles', views.RolesView, 'roles')
router.register(r'permisoruta',views.PermisoRutasView,'permisoruta' )
router.register(r'rutas',views.RutasView,'ruta' )
router.register(r'categoriarespuesto',views.CategoriaRepuestoView,'categoriarepuesto')
router.register(r'repuesto',views.RepuestoView,'repuesto' )
router.register(r'ordentrabajo',views.OrdenTrabajoView, 'ordentrabajo')

urlpatterns = [
    path('', include(router.urls)),
    #path('docs/', include_docs_urls(title='usuarios api')),
]
