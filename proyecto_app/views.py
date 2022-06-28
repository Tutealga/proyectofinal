from urllib import request
import django
from django.shortcuts import render, redirect
from proyecto_app.models import Productos, Usuario_perfil, Descripcion
from proyecto_app.forms import Usuarios_form, Productos_form, Descripcion_form

from django.views.generic import DetailView, DeleteView, UpdateView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from proyecto_app.forms import User_registration_form

from django.urls import reverse

class Detalle_productos(DetailView):
    model = Productos
    template_name = 'detalle_productos.html'

class Borrar_productos(DeleteView):
    model = Productos
    template_name = 'borrar_productos.html'
    def get_success_url(self):
        return reverse('productos')

class Editar_productos(UpdateView):
    model = Productos
    template_name = 'editar_productos.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_producto', kwargs = {'pk':self.object.pk})

# Vista productos
def productos(request):
    productos = Productos.objects.all()
    context = {'productos':productos}
    return render(request, 'productos.html', context = context)

# Vista usuarios
def usuarios(request):
    usuarios = Usuario_perfil.objects.all()
    context = {'usuario_perfil':usuarios}
    return render(request, 'usuarios.html', context = context)

# Vista comentarios
def descripcion(request):
    descripcion = Descripcion.objects.all()
    context = {'descripcion':descripcion}
    return render(request, 'descripcion.html', context = context)

# Vista para buscar entre modelos
def buscar(request):
    buscar_productos = Productos.objects.filter(nombre__icontains = request.GET['search'])
    buscar_usuarios = Usuarios.objects.filter(nombre__icontains = request.GET['search'])
    context = {'buscar_productos':buscar_productos,'buscar_usuarios':buscar_usuarios}
    return render(request, 'buscar.html', context = context)

# Vista crear nuevo usuario
def nuevo_usuario(request):
    if request.method == 'GET':
        form = Usuarios_form()
        context = {'form':form}
        return render(request, 'nuevo_usuario.html', context=context)
    else:
        form = Usuarios_form(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuarios.objects.create(
                nombre = form.cleaned_data['nombre'],
                edad = form.cleaned_data['edad'],
                fecha_alta = form.cleaned_data['fecha_alta'],
                DNI = form.cleaned_data['DNI'],
            )

            context ={'nuevo_usuario':nuevo_usuario}
        return render(request, 'nuevo_usuario.html', context=context)

# Vista crear nuevo producto
def nuevo_producto(request):
  if request.user.is_authenticated and request.user.is_superuser:
    if request.method == 'GET':
        form = Productos_form()
        context = {'form':form}
        return render(request, 'nuevo_producto.html', context=context)
    else:
        form = Productos_form(request.POST)
        if form.is_valid():
            nuevo_producto = Productos.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                SKU = form.cleaned_data['SKU'],
                stock = form.cleaned_data['stock'],
            )
  
            context ={'nuevo_producto':nuevo_producto}
        return render(request, 'nuevo_producto.html', context=context)
  else:
        return redirect('login')

# Vista crear nuevo comentario
def nuevo_descripcion(request):
    if request.method == 'GET':
        form = Descripcion_form()
        context = {'form':form}
        return render(request, 'nuevo_descripcion.html', context=context)
    else:
        form = Descripcion_form(request.POST)
        if form.is_valid():
            nuevo_descripcion = Descripcion.objects.create(
                comentario = form.cleaned_data['comentario'],
                puntuacion = form.cleaned_data['puntuacion'],
                usuario = form.cleaned_data['usuario'],
            )

            context ={'nuevo_descripcion':nuevo_descripcion}
        return render(request, 'nuevo_descripcion.html', context=context)

#Vista para Login/Logout/Register
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}!! :D'}
                return redirect('index')
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente {username}'}
            return redirect('index')
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)

def logout_view(request):
    logout(request)
    return redirect('index')

