from django.urls import path

from proyecto_app.views import nuevo_descripcion, nuevo_producto, productos, usuarios, descripcion, buscar, nuevo_usuario, nuevo_producto, nuevo_descripcion

urlpatterns = [
    path("productos/", productos, name="productos"),
    path("usuarios/", usuarios, name="usuarios"),
    path("descripcion/", descripcion, name="descripcion"),
    path("buscar/", buscar, name="buscar"),
    path("nuevo_usuario/", nuevo_usuario, name="nuevo_usuario"),
    path("nuevo_producto/", nuevo_producto, name="nuevo_producto"),
    path("nuevo_comentario/", nuevo_descripcion, name="nuevo_descripcion"),
]