from django import forms  # Importando el módulo 'forms' de Django
from django.contrib.auth.forms import UserCreationForm  # Importando el formulario de creación de usuario proporcionado por Django
from django.contrib.auth.models import User  # Importando el modelo de usuario de Django

class CustomUserCreationFrom(UserCreationForm):
    # Definición de una clase personalizada 'CustomUserCreationFrom' que hereda de 'UserCreationForm'

    class Meta:
        # La clase 'Meta' se utiliza para configurar metadatos de un modelo o formulario
        model = User
        # Especifica que el modelo relacionado a este formulario es el modelo de usuario predeterminado de Django
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # Especifica qué campos del modelo de usuario deben mostrarse en el formulario de registro.
    pass
    # La declaración 'pass' simplemente indica que esta clase está vacía y no contiene ningún método personalizado. Utiliza la implementación predeterminada de 'UserCreationForm' para manejar la creación de usuarios.
