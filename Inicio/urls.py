from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('kdjsmnskd', views.base, name='base'),
    path('Registro', views.registro, name='registro')
    #path('agregar/', views.agregar_evento, name='agregar_evento'),
    #path('eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    #path('detalle/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    #path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
]