from urllib import request
from django.shortcuts import render
from proyecto_app.models import Productos, Usuarios, Descripcion

# Create your views here.

def productos(request):
    productos = Productos.objects.all()
    context = {'productos':productos}
    return render(request, 'productos.html', context = context)

def usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {'usuarios':usuarios}
    return render(request, 'usuarios.html', context = context)

def descripcion(request):
    descripcion = Descripcion.objects.all()
    context = {'descripcion':descripcion}
    return render(request, 'descripcion.html', context = context)

def buscar_productos(request):
    buscar_productos = Productos.objects.filter(nombre__icontains = request.GET['search'])
    context = {'buscar_productos':buscar_productos}
    return render(request, 'buscar_productos.html', context = context)



