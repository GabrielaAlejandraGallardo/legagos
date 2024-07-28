from socket import fromshare
from django import forms 
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields='__all__'
        
        def clean_archivo(self):  
          archivo = self.cleaned_data.get('archivo')  
          if archivo:  
            if not archivo.name.endswith('.pdf'):  
                raise forms.ValidationError("Solo se permiten archivos PDF.")  
          return archivo  