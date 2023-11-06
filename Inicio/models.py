from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=15)  # Campo para el número de teléfono
    institucion = models.CharField(max_length=100)  # Campo para la institución
    eventos_asistira = models.ManyToManyField('Evento')  # Campo para los eventos a los que asistirá
    foto_de_perfil = models.ImageField(upload_to='fotosPerfiles/', default='user.webp') #Foto de perfil de usuario
    # Agrega related_name para evitar conflictos en los campos inversos de grupos y permisos
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set')

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)