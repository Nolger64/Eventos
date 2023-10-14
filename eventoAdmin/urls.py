from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('agregar/', views.agregar_evento, name='agregar_evento'),
    path('eventos/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('eventos/detalle/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
]