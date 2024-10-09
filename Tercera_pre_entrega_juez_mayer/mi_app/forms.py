from django import forms
from .models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    autor_nombre = forms.CharField(max_length=100, label="Nombre del Autor")
    autor_apellido = forms.CharField(max_length=100, label="Apellido del Autor")
    editorial_nombre = forms.CharField(max_length=100, label="Nombre de la Editorial")
    
    class Meta:
        model = Libro
        fields = ['titulo', 'isbn', 'fecha_publicacion', 'stock', 'imagen_url', 'autor_nombre', 'autor_apellido', 'editorial_nombre']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        # Llama al constructor de la clase padre
        super().__init__(*args, **kwargs)
        
        if self.instance.pk:  # Verifica si ya hay una instancia del libro
            self.fields['autor_nombre'].initial = self.instance.autor.nombre
            self.fields['autor_apellido'].initial = self.instance.autor.apellido
            self.fields['editorial_nombre'].initial = self.instance.editorial.nombre

    def save(self, commit=True):
        libro = super().save(commit=False)
        autor_nombre = self.cleaned_data['autor_nombre']
        autor_apellido = self.cleaned_data['autor_apellido']
        editorial_nombre = self.cleaned_data['editorial_nombre']

        # Busca o crea el autor
        autor, created = Autor.objects.get_or_create(nombre=autor_nombre, apellido=autor_apellido)
        libro.autor = autor

        # Busca o crea la editorial
        editorial, created = Editorial.objects.get_or_create(nombre=editorial_nombre)
        libro.editorial = editorial

        if commit:
            libro.save()
        return libro

    
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
