from django import forms
from .models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'isbn', 'fecha_publicacion']
        widget = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        isbn = cleaned_data.get('isbn')

        if not titulo:
            raise forms.ValidationError('El titulo es obligatorio.')
        if not isbn:
            raise forms.ValidationError('El ISBN es obligatorio.')
        
        return cleaned_data

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']

class BusquedaLibroForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True, label='Buscar libros')
