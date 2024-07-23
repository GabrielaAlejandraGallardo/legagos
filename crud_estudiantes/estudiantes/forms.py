from socket import fromshare
from django import forms 
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields='__all__'