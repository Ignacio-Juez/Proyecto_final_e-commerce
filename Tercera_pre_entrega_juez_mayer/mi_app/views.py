# mi_app/views.py
from django.shortcuts import render, redirect
from .forms import BusquedaLibroForm
from .forms import LibroForm, AutorForm, EditorialForm
from .models import Libro, Autor, Editorial

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def agregar_libro(request):
    if request.method == 'POST':
        libro_form = LibroForm(request.POST)
        autor_form = AutorForm(request.POST)
        editorial_form = EditorialForm(request.POST)

        if libro_form.is_valid() and autor_form.is_valid() and editorial_form.is_valid():
            autor = autor_form.save()
            editorial = editorial_form.save()

            libro = libro_form.save(commit=False)
            libro.autor = autor
            libro.editorial = editorial
            libro.save()

            return redirect('index')
        else: 
            return render(request, 'agregar_libro.html',{
                'libro_form': libro_form,
                'autor_form': autor_form,
                'editorial_form': editorial_form
            })

    else:
        libro_form = LibroForm()
        autor_form = AutorForm()
        editorial_form = EditorialForm()

    return render(request, 'agregar_libro.html', {
        'libro_form': libro_form,
        'autor_form': autor_form,
        'editorial_form': editorial_form
    })

def buscar_libro(request):
    resultados = None
    busqueda_realizada = False
    form = BusquedaLibroForm()

    if request.method == 'GET':
        titulo = request.GET.get('titulo', None)
        if titulo:
            resultados = Libro.objects.filter(titulo__icontains=titulo)
            busqueda_realizada = True
    return render(request, 'buscar_libro.html', {
        'form': form,
        'resultados': resultados,
        'busqueda_realizada': busqueda_realizada
    })

