from django import forms  # Importando el módulo 'forms' de Django
from django.contrib.auth.forms import UserCreationForm  # Importando el formulario de creación de usuario proporcionado por Django
from .models import CustomUser  # Importando el modelo de usuario de Django

class PhotoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['foto_de_perfil']

class CustomUserCreationForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=True)  # Campo para el número de teléfono
    institucion = forms.CharField(max_length=100, required=True)  # Campo para la institución

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'institucion', 'password1', 'password2']