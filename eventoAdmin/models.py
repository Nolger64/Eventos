from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, default="")
    fecha = models.DateField()
    hora = models.TimeField(null=True)
    descripcion = models.TextField()