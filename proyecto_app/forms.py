from django import forms
from proyecto_app.models import Descripcion, Productos, Usuario_perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Formulario para crear usuarios
class Usuarios_form(forms.ModelForm):
    class Meta:
        model = Usuario_perfil
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


#Formulario para crear usuarios login/register
class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
