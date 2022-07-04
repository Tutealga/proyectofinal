from django.contrib import admin

from proyecto_app.models import Productos, Descripcion, Usuario_perfil, ModificacionesInicio

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display= ['nombre','precio','SKU','stock']

@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display= ['comentario','puntuacion','usuario']

@admin.register(Usuario_perfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display= ['usuario','telefono','imagen']

@admin.register(ModificacionesInicio)
class ModificacionesInicioAdmin(admin.ModelAdmin):
    list_display= ['titulo','descripcion','banner']

