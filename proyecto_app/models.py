from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Usuario_perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='profile_image', default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

# Modelo productos
class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
# Modelo comentarios   
class Descripcion(models.Model):
    comentario = models.TextField()
    puntuacion = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #avatar = models.ForeignKey(Usuario_perfil, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'descripcion'
        verbose_name_plural = 'descripciones'
