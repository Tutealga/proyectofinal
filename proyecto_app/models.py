from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_alta = models.CharField(max_length=200, blank=True, null=True)
    DNI = models.CharField(max_length=30, unique=True)
    
class Descripcion(models.Model):
    comentario = models.CharField(max_length=500)
    puntuacion = models.IntegerField()
    