from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class ModificacionesInicio(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    banner = models.ImageField(upload_to='banner_image')

    class Meta:
        verbose_name = 'modificacion inicio'
        verbose_name_plural = 'modificaciones inicio'

class Usuario_perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='profile_image', default='profile_image/descarga.png')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

# Modelo productos
class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='producto_image', default='producto_image/descarga.png')

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
# Modelo comentarios   
class Descripcion(models.Model):
    comentario = models.TextField()
    puntuacion = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'descripcion'
        verbose_name_plural = 'descripciones'
