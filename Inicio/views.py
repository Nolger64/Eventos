from django.shortcuts import render, redirect
from eventoAdmin.models import Evento, Asistente  # Importando el modelo 'Evento' (asegúrate de que el import sea correcto)
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserCreationForm, PhotoForm  # Importando formularios
from django.contrib.auth import authenticate, login  # Funciones de autenticación



#--------------------------------------------------------------------------------------------------#
@login_required  # Decorador: Requiere que el usuario esté autenticado para acceder a esta vista
def base(request): #Vista para la base de la pagina web
    return render(request, 'base.html')  # Renderiza la plantilla 'base.html'
#--------------------------------------------------------------------------------------------------#
@login_required #Aun trabajo en esto
def evetosPorAsistir(request):
    return render(request, 'porAsistir.html')
#--------------------------------------------------------------------------------------------------#
#Vista para la página de inicio del usuario autenticado.
#Permite cambiar la foto de perfil del usuario.
#Da informacion del usuario y premite ver los eventos en los que esta registrado(En desarrollo)
@login_required
def inicio(request): 
    #Obtengo el usuario actual
    user = request.user
    # Obtiene todos los eventos de la base de datos
    eventos = Evento.objects.all()
    # Procesa el formulario para cambiar la foto de perfil 
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a la página de inicio después de guardar la foto
    else:
        form = PhotoForm(instance=user)  # Carga el formulario con la instancia del usuario actual
    return render(request, 'inicio.html', {'eventos': eventos, 'form': form, 'user': user})
#--------------------------------------------------------------------------------------------------#
#Esta parte permite registrar usuario con rol de asistentes
def registro(request): #Vista para el registro de nuevos usuarios.
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save()  # Guarda el nuevo usuario en la base de datos
            # Asigna los valores de los campos adicionales
            user.telefono = user_creation_form.cleaned_data['telefono']
            user.institucion = user_creation_form.cleaned_data['institucion']
            user.save()  # Guarda los campos adicionales en el usuario
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio después del registro exitoso
    return render(request, 'register.html', data)
#--------------------------------------------------------------------------------------------------#