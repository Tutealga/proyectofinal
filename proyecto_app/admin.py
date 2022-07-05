from django.contrib import admin

from proyecto_app.models import Productos, Descripcion, Usuario_perfil, ModificacionesInicio


#Mostrar productos en el admin con sus campos para modificar
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display= ['nombre','precio','SKU','stock']

#Mostrar comentarios en el admin con sus campos para modificar
@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display= ['comentario','puntuacion','usuario']

#Mostrar perfiles de usuarios en el admin con sus campos para modificar
@admin.register(Usuario_perfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display= ['usuario','telefono','imagen']

#Mostrar las modificaciones del index en el admin con sus campos para modificar
@admin.register(ModificacionesInicio)
class ModificacionesInicioAdmin(admin.ModelAdmin):
    list_display= ['titulo','descripcion','banner']

