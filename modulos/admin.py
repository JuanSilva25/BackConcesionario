from django.contrib import admin
from .models import Usuario
from .models import Roles

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Roles)