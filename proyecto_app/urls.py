from django.urls import path
from proyecto_app.views import about, Edit_username_password, CambiarContraseña, Borrar_Usuario_perfil, Detalle_Usuario_perfil, Editar_Usuario_perfil, nuevo_producto, productos, usuarios, buscar, nuevo_producto, Detalle_productos, Borrar_productos, Editar_productos, login_view, logout_view, register_view

urlpatterns = [
    #Urls para mostrar los elementos
    path("about/", about, name="productos"),
    path("productos/", productos, name="productos"),
    path("usuarios/", usuarios, name="usuarios"),
    path("buscar/", buscar, name="buscar"),

    #Urls de productos
    path("nuevo_producto/", nuevo_producto, name="nuevo_producto"),
    path('detalle-productos/<int:pk>/', Detalle_productos.as_view(), name="detalle_producto"),
    path('borrar-productos/<int:pk>/', Borrar_productos.as_view(), name="borrar_producto"),
    path('editar-productos/<int:pk>/', Editar_productos.as_view(), name="editar_productos"),

    #Urls de usuarios
    path('detalle-usuario-perfil/<int:pk>/', Detalle_Usuario_perfil.as_view(), name="detalle_usuario_perfil"),
    path('borrar-usuario-perfil/<int:pk>/', Borrar_Usuario_perfil.as_view(), name="borrar_usuario_perfil"),
    path('editar-usuario-perfil/<int:pk>/', Editar_Usuario_perfil.as_view(), name="editar_usuario_perfil"),
    path('editar-usuario/<int:pk>/', Edit_username_password.as_view(), name='editar_usuario'),
    path('editar-usuario/password/', CambiarContraseña.as_view(template_name='auth/cambiar-contraseña.html')),

    #Urls de login/registro/logout
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('registrarse/', register_view, name = 'register'),
]