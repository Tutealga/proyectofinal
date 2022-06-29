from django.http import HttpResponse
from django.shortcuts import render, redirect

from proyecto_app.forms import Descripcion_form
from proyecto_app.models import Descripcion, Productos
from proyecto_app.views import usuarios

def index(request):
    descripcion = Descripcion.objects.all()
    productos = Productos.objects.all()
    if request.method == 'GET':
        form = Descripcion_form()
        context = {'form':form,'descripcion':descripcion,'productos':productos}
        return render(request, 'index.html', context=context)
    else:
     if request.user.is_authenticated: 
        form = Descripcion_form(request.POST)
        if form.is_valid():
            nuevo_descripcion = Descripcion.objects.create(
                comentario = form.cleaned_data['comentario'],
                puntuacion = form.cleaned_data['puntuacion'],
                usuario = request.user
            )

            context ={'descripcion':descripcion,'productos':productos}
        return redirect('index')
     else:
        context ={'errors':'Debes estar logiado para dejar un comentario'}
        return render(request, 'index.html', context=context)
        
