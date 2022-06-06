from urllib import request
from django.shortcuts import render
from proyecto_app.models import Productos, Usuarios, Descripcion
from proyecto_app.forms import Usuarios_form, Productos_form, Descripcion_form

# Vista productos
def productos(request):
    productos = Productos.objects.all()
    context = {'productos':productos}
    return render(request, 'productos.html', context = context)

# Vista usuarios
def usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {'usuarios':usuarios}
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
    buscar_descripciones = Descripcion.objects.filter(id__icontains = request.GET['search'])
    context = {'buscar_productos':buscar_productos,'buscar_usuarios':buscar_usuarios,'buscar_descripciones':buscar_descripciones}
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
            )

            context ={'nuevo_descripcion':nuevo_descripcion}
        return render(request, 'nuevo_descripcion.html', context=context)


