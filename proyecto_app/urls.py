from django.urls import path

from proyecto_app.views import nuevo_descripcion, nuevo_producto, productos, usuarios, descripcion, buscar, nuevo_usuario, nuevo_producto, nuevo_descripcion, Detalle_productos, Borrar_productos, Editar_productos

urlpatterns = [
    path("productos/", productos, name="productos"),
    path("usuarios/", usuarios, name="usuarios"),
    path("descripcion/", descripcion, name="descripcion"),
    path("buscar/", buscar, name="buscar"),
    path("nuevo_usuario/", nuevo_usuario, name="nuevo_usuario"),
    path("nuevo_producto/", nuevo_producto, name="nuevo_producto"),
    path("nuevo_comentario/", nuevo_descripcion, name="nuevo_descripcion"),

    path('detalle-productos/<int:pk>/', Detalle_productos.as_view(), name="detalle_producto"),
    path('borrar-productos/<int:pk>/', Borrar_productos.as_view(), name="borrar_producto"),
    path('editar-productos/<int:pk>/', Editar_productos.as_view(), name="editar_productos"),
]