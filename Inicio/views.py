from django.shortcuts import render
from eventoAdmin.models import Evento
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    return render(request, 'base.html')

@login_required
def inicio(request):
    eventos = Evento.objects.all() # Paso 1: Obtener todos los eventos de la base de datos
    totalReg = Evento.objects.latest('id') # Obtén el último registro en la tabla
    ultimo_id = totalReg.id # Accede al ID del último registro
    return render(request, 'inicio.html', {'eventos': eventos, 'total' : ultimo_id})

