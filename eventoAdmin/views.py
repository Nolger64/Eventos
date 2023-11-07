from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Asistente # modelos de evento
from .forms import EventoForm  # Crear un formulario para agregar eventos
from django.contrib.auth.decorators import login_required, user_passes_test # Importando modulos de iniciar sesion

#Para indentificar ROL del usuario
def es_staff(user):
    return user.is_staff

@login_required # Sesion de administrador necesaria
def lista_eventos(request):
    eventos = Evento.objects.all() # Paso 1: Obtener todos los eventos de la base de datos
    form = EventoForm() # Paso 2: Crear una instancia del formulario para agregar eventos
    # Paso 4: Renderizar la plantilla HTML y pasar los eventos y el formulario
    return render(request, 'listaEventos.html', {'eventos': eventos, 'form': form})

@user_passes_test(es_staff)
@login_required # Sesion de administrador necesaria
def agregar_evento(request):
    eventos = Evento.objects.all() # Paso 1: Obtener todos los eventos de la base de datos
    form = EventoForm() # Paso 2: Crear una instancia del formulario para agregar eventos

    if request.method == 'POST': # Paso 3: Procesar el formulario cuando se envía
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el evento en la base de datos
            return redirect('lista_eventos')  # Redirigir a la misma página después de agregar
    return render(request, 'agregarEvento.html', {'eventos': eventos, 'form': form})

@user_passes_test(es_staff)
@login_required # Sesion de administrador necesaria
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'editarEvento.html', {'form': form})

@user_passes_test(es_staff)
@login_required # Sesion de administrador necesaria
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    
    return render(request, 'eliminarEvento.html', {'evento': evento})

@login_required # Sesion de administrador necesaria
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    esta_asistiendo = Asistente.objects.filter(usuario=request.user, evento=evento).exists()
    return render(request, 'detalleEvento.html', {'evento': evento, 'esta_asistiendo': esta_asistiendo})

@login_required
def unirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    asistente, creado = Asistente.objects.get_or_create(usuario=request.user, evento=evento)
    if creado:
        asistente.save()
    return redirect('detalle_evento', evento_id=evento_id)

@login_required
def abandonar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    Asistente.objects.filter(usuario=request.user, evento=evento).delete()
    return redirect('detalle_evento', evento_id=evento_id)


