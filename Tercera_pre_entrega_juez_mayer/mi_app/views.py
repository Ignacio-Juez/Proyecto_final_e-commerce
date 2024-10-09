from django.shortcuts import render, redirect
from .forms import LibroForm, AutorForm, EditorialForm
from .models import Libro, Autor, Editorial
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404

def index(request):
    is_employee = request.user.groups.filter(name='empleados').exists() if request.user.is_authenticated else False
    libros = Libro.objects.all() 
    return render(request, 'index.html', {'is_employee': is_employee, 'libros': libros})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        
        email_content = f"Nuevo mensaje de contacto:\n\nNombre: {name}\nEmail: {email}\nAsunto:{subject}\nMensaje: {message}"

        
        email_message = EmailMessage(
            subject,
            email_content,  
            settings.EMAIL_HOST_USER,
            ['ignacio09098@gmail.com']
        )
        email_message.fail_silently = False
        email_message.send()

        messages.success(request, "Se ha enviado correctamente su correo.")
        return redirect('contact')

    else:
        return render(request, 'contact.html')

def is_employee(user):
    return user.groups.filter(name='empleados').exists()

@login_required
@user_passes_test(is_employee)
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
        libro_form = LibroForm()
        autor_form = AutorForm()
        editorial_form = EditorialForm()

    return render(request, 'agregar_libro.html', {
        'libro_form': libro_form,
        'autor_form': autor_form,
        'editorial_form': editorial_form
    })

@login_required
@user_passes_test(is_employee)
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        libro_form = LibroForm(request.POST, instance=libro)
        if libro_form.is_valid():
            libro_form.save()
            return redirect('gestionar_libros')
    else:
        libro_form = LibroForm(instance=libro)

    return render(request, 'editar_libro.html', {'libro_form': libro_form})


@login_required
@user_passes_test(is_employee)
def gestionar_libros(request):
    libros = Libro.objects.all()  
    return render(request, 'gestionar_libros.html', {'libros': libros})

@login_required
@user_passes_test(is_employee)
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    libro.delete()
    return redirect('gestionar_libros')


def buscar_libro(request):
    titulo = request.GET.get('titulo', '')  
    if titulo:
        resultados = Libro.objects.filter(titulo__icontains=titulo)  
        busqueda_realizada = True
    else:
        resultados = Libro.objects.all()  
        busqueda_realizada = False

    return render(request, 'buscar_libro.html', {
        'resultados': resultados,
        'busqueda_realizada': busqueda_realizada
    })

def detalles_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    
    return render(request, 'detalles_libro.html', {'libro': libro})

