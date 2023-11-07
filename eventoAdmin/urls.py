from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('agregar/', views.agregar_evento, name='agregar_evento'),
    path('eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('detalle/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('unirse/<int:evento_id>/', views.unirse_evento, name='unirse_evento'),
    path('abandonar/<int:evento_id>/', views.abandonar_evento, name='abandonar_evento'),
]