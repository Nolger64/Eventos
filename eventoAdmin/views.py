from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento # modelos de evento
from .forms import EventoForm  # Crear un formulario para agregar eventos

def lista_eventos(request):
    eventos = Evento.objects.all() # Paso 1: Obtener todos los eventos de la base de datos
    form = EventoForm() # Paso 2: Crear una instancia del formulario para agregar eventos

    # Paso 4: Renderizar la plantilla HTML y pasar los eventos y el formulario
    return render(request, 'listaEventos.html', {'eventos': eventos, 'form': form})

def agregar_evento(request):
    eventos = Evento.objects.all() # Paso 1: Obtener todos los eventos de la base de datos
    form = EventoForm() # Paso 2: Crear una instancia del formulario para agregar eventos

    if request.method == 'POST': # Paso 3: Procesar el formulario cuando se envía
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el evento en la base de datos
            return redirect('lista_eventos')  # Redirigir a la misma página después de agregar
    return render(request, 'agregarEvento.html', {'eventos': eventos, 'form': form})

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

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    
    return render(request, 'eliminarEvento.html', {'evento': evento})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'detalleEvento.html', {'evento': evento})

