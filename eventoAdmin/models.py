from django.db import models
from django.conf import settings

class Evento(models.Model):
    activo = models.BooleanField(default=True)
    titulo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, default="")
    fecha = models.DateField()
    hora = models.TimeField(null=True)
    descripcion = models.TextField()

class Asistente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)