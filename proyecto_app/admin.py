from django.contrib import admin

from proyecto_app.models import Productos, Descripcion, Usuario_perfil


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display= ['nombre','precio','SKU','stock']

@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display= ['comentario','puntuacion','usuario']

admin.site.register(Usuario_perfil)
