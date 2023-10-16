from django.contrib import admin
from .models import Usuario,Roles,PermisoRutas,Rutas,CategoriaRepuesto,Repuesto,OrdenTrabajo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Roles)
admin.site.register(PermisoRutas)
admin.site.register(CategoriaRepuesto)
admin.site.register(Repuesto)
admin.site.register(Rutas)
admin.site.register(OrdenTrabajo)