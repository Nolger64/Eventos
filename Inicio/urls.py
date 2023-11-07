from django.urls import path #Necesario para las rutas
from . import views #Importa las todas las vista de la aplicacion inicio

urlpatterns = [
    path('', views.inicio, name='inicio'), #Configura la url de la pagina de inicio
    path('base/', views.base, name='base'), #Configura la url de la pagina base de la aplicacion
    path('registro', views.registro, name='registro'), #Configura la url de la pagina de registro
    path('porAsistir', views.evetosPorAsistir, name='por_asistir') #Configura la url de la pagina de eventos por asistir
]