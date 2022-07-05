from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from proyecto_app.models import Usuario_perfil


#Este archivo y codigos crea automaticamente el perfil de usuario (Usuario_perfil) al registrarse
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Usuario_perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.usuario_perfil.save()
