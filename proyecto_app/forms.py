from django import forms
from proyecto_app.models import Descripcion, Productos, Usuarios

# Formulario para crear usuarios
class Usuarios_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

# Formulario para crear productos
class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

# Formulario para crear comentarios
class Descripcion_form(forms.ModelForm):
    class Meta:
        model = Descripcion
        fields = '__all__'