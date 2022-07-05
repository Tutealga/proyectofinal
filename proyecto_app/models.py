from email.policy import default
from django.db import models
from django.contrib.auth.models import User

#Modelo de las modificaciones del index
class ModificacionesInicio(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    banner = models.ImageField(upload_to='banner_image')

    class Meta:
        verbose_name = 'modificacion inicio'
        verbose_name_plural = 'modificaciones inicio'

#Modelo del perfil de usuario
class Usuario_perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    web = models.URLField(max_length=300, null=True, blank=True)
    imagen = models.ImageField(upload_to='profile_image', default='profile_image/descarga.png')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        
# Modelo de los productos
class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='producto_image', default='producto_image/descarga.png')

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
# Modelo de los comentarios   
class Descripcion(models.Model):
    opciones = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
    ("8", "8"), 
    ("9", "9"),
    ("10", "10"),
) 
    comentario = models.TextField()
    puntuacion = models.CharField(default=1, choices=opciones, max_length=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='descripcion_image')
    
    class Meta:
        verbose_name = 'descripcion'
        verbose_name_plural = 'descripciones'
