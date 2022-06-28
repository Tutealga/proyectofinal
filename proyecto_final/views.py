from django.http import HttpResponse
from django.shortcuts import render, redirect

from proyecto_app.forms import Descripcion_form
from proyecto_app.models import Descripcion, Productos

def index(request):
    descripcion = Descripcion.objects.all()
    productos = Productos.objects.all()
    if request.method == 'GET':
        form = Descripcion_form()
        context = {'form':form,'descripcion':descripcion,'productos':productos}
        return render(request, 'index.html', context=context)
    else:
        form = Descripcion_form(request.POST)
        if form.is_valid():
            nuevo_descripcion = Descripcion.objects.create(
                comentario = form.cleaned_data['comentario'],
                puntuacion = form.cleaned_data['puntuacion'],
                usuario = form.cleaned_data['usuario'],
            )

            context ={'descripcion':descripcion,'productos':productos}
        return redirect('index')
