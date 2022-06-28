from django.db import models
from django.contrib.auth.models import User

class Usuario_perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='profile_image')

# Modelo productos
class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)
    
# Modelo comentarios   
class Descripcion(models.Model):
    comentario = models.CharField(max_length=500)
    puntuacion = models.IntegerField(default=1)
    usuario = models.ForeignKey('Usuario_perfil',on_delete=models.CASCADE,related_name="usuario_perfil")
    