from distutils.command import upload
from django import forms
from proyecto_app.models import Descripcion, Productos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

# Formulario para crear productos
class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

# Formulario para crear comentarios
class Descripcion_form(forms.ModelForm):
    comentario = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Deja tu comentario...',
        'rows': '4',
    }))
    class Meta:
        model = Descripcion
        fields = ['comentario','puntuacion']

#Formulario para crear usuarios (register)
class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

#Formulario para modificar usuarios (username y email)
class Editar_usuario(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput() )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email"]

