from django.contrib import admin
from .models import Libro, Autor, Editorial

# Modelo admin
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'isbn', 'fecha_publicacion', 'stock')
    search_fields = ('titulo', 'isbn')
    list_filter = ('autor', 'editorial')

# Modelo Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

# Modelo Editorial
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

