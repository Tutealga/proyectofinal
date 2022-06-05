from django.urls import path

from proyecto_app.views import productos, usuarios, descripcion, buscar_productos

urlpatterns = [
    path("productos/", productos, name="productos"),
    path("usuarios/", usuarios, name="usuarios"),
    path("descripcion/", descripcion, name="descripcion"),
    path("buscar-productos/", buscar_productos, name="buscar_productos")
]