from django.shortcuts import render
from eventoAdmin.models import Evento
from django.contrib.auth.decorators import login_required # Importando modulos de iniciar sesion

@login_required # Sesion de administrador necesaria
def base(request):
    return render(request, 'base.html')

@login_required # Sesion de administrador necesaria
def inicio(request):
    eventos = Evento.objects.all() # Paso 1: Obtener todos los eventos de la base de datos
    totalReg = Evento.objects.latest('id') # Obtén el último registro en la tabla
    ultimo_id = totalReg.id # Accede al ID del último registro
    return render(request, 'inicio.html', {'eventos': eventos, 'total' : ultimo_id})

