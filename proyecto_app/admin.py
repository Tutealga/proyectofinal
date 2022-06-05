from django.contrib import admin

from proyecto_app.models import Productos, Usuarios, Descripcion
# Register your models here.

admin.site.register(Productos)
admin.site.register(Usuarios)
admin.site.register(Descripcion)