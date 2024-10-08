from django.contrib import admin
from .models import Libro, Autor, Editorial

# Registra el modelo Libro en el admin
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'isbn', 'fecha_publicacion', 'stock')
    search_fields = ('titulo', 'isbn')
    list_filter = ('autor', 'editorial')

# Registra el modelo Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

# Registra el modelo Editorial
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
# Register your models here.
