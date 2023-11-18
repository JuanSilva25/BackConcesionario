
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from models import Usuario, Roles

content_type = ContentType.objects.get_for_model(Usuario)

# Crear permisos
perm_ver_cotizaciones = Permission.objects.create(
    codename='ver_cotizaciones',
    name='Puede ver cotizaciones',
    content_type=content_type,
)

perm_ver_ordenes_de_trabajo = Permission.objects.create(
    codename='ver_ordenes_de_trabajo',
    name='Puede ver órdenes de trabajo',
    content_type=content_type,
)

admin_role = Roles.objects.get(rol='Administrador')
vendedor_role = Roles.objects.get(rol='Vendedor')
jefe_taller_role = Roles.objects.get(rol='Jefe de Taller')

admin_role.permissions.add(perm_ver_cotizaciones, perm_ver_ordenes_de_trabajo)
vendedor_role.permissions.add(perm_ver_cotizaciones)
jefe_taller_role.permissions.add(perm_ver_ordenes_de_trabajo)
