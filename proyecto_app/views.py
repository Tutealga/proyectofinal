from urllib import request
import django
from django.shortcuts import render, redirect
from proyecto_app.models import ModificacionesInicio, Productos, Usuario_perfil, Descripcion
from proyecto_app.forms import Productos_form

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

class Detalle_Usuario_perfil(DetailView):
    model = Usuario_perfil
    template_name = 'detalle_usuario_perfil.html'

class Borrar_Usuario_perfil(DeleteView):
    model = Usuario_perfil
    template_name = 'borrar_usuario_perfil.html'
    def get_success_url(self):
        return reverse('productos')

class Editar_Usuario_perfil(UpdateView):
    model = Usuario_perfil
    template_name = 'editar_usuario_perfil.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_usuario_perfil', kwargs = {'pk':self.object.pk})

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

# Vista para buscar entre modelos
def buscar(request):
    buscar_productos = Productos.objects.filter(nombre__icontains = request.GET['search'])
    context = {'buscar_productos':buscar_productos}
    return render(request, 'buscar.html', context = context)

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
       return redirect('index')

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
  if request.user.is_authenticated:
    logout(request)
    return redirect('index')



