from django.urls import path

from proyecto_app.views import Borrar_Usuario_perfil, Detalle_Usuario_perfil, Editar_Usuario_perfil, nuevo_producto, productos, usuarios, descripcion, buscar, nuevo_producto, Detalle_productos, Borrar_productos, Editar_productos, login_view, logout_view, register_view

urlpatterns = [
    path("productos/", productos, name="productos"),
    path("usuarios/", usuarios, name="usuarios"),
    path("descripcion/", descripcion, name="descripcion"),
    path("buscar/", buscar, name="buscar"),
    path("nuevo_producto/", nuevo_producto, name="nuevo_producto"),

    path('detalle-productos/<int:pk>/', Detalle_productos.as_view(), name="detalle_producto"),
    path('borrar-productos/<int:pk>/', Borrar_productos.as_view(), name="borrar_producto"),
    path('editar-productos/<int:pk>/', Editar_productos.as_view(), name="editar_productos"),
    path('detalle-usuario-perfil/<int:pk>/', Detalle_Usuario_perfil.as_view(), name="detalle_usuario_perfil"),
    path('borrar-usuario-perfil/<int:pk>/', Borrar_Usuario_perfil.as_view(), name="borrar_usuario_perfil"),
    path('editar-usuario-perfil/<int:pk>/', Editar_Usuario_perfil.as_view(), name="editar_usuario_perfil"),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),

]