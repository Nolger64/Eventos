from django.shortcuts import render  # Importando el módulo para renderizar plantillas
from eventoAdmin.models import Evento  # Importando el modelo 'Evento'
from django.contrib.auth.decorators import login_required  # Importando los decoradores de autenticación
from .forms import CustomUserCreationFrom  # Importando el formulario de registro de usuario
from django.shortcuts import redirect  # Importando la función de redirección
from django.contrib.auth import authenticate, login  # Importando funciones de autenticación

@login_required  # Decorador: Requiere que el usuario esté autenticado para acceder a esta vista
def base(request):
    return render(request, 'base.html')  # Renderiza la plantilla 'base.html'

@login_required  # Decorador: Requiere que el usuario esté autenticado para acceder a esta vista
def inicio(request):
    eventos = Evento.objects.all()  # Obtiene todos los eventos de la base de datos
    totalReg = Evento.objects.latest('id')  # Obtiene el registro más reciente en la tabla 'Evento'
    ultimo_id = totalReg.id  # Obtiene el ID del último registro
    return render(request, 'inicio.html', {'eventos': eventos, 'total': ultimo_id})  # Renderiza la plantilla 'inicio.html' y pasa datos de eventos y el último ID como contexto

def registro(request):  # Definición de una vista llamada 'registro' para el registro de usuarios
    data = {
        'form': CustomUserCreationFrom()  # Inicializa un diccionario 'data' con un formulario de registro vacío
    }
    if request.method == 'POST':  # Comprueba si la solicitud HTTP es de tipo POST (envío de datos del formulario)
        user_creation_form = CustomUserCreationFrom(data=request.POST)  # Crea una instancia del formulario con los datos POST
        if user_creation_form.is_valid():  # Comprueba si el formulario es válido
            user_creation_form.save()  # Guarda el nuevo usuario en la base de datos
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            # Autentica al nuevo usuario
            login(request, user)  # Inicia la sesión del usuario después del registro exitoso
            return redirect('inicio')  # Redirige al usuario a la página 'inicio' después del registro exitoso
    return render(request, 'register.html', data)  # Renderiza la página 'register.html' con el formulario (solicitud GET) o con errores de validación (solicitud POST)
