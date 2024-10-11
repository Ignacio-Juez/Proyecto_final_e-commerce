from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroForm, AutorForm, EditorialForm
from .models import Libro, Autor, Editorial, Carrito
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


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

        
        print("Datos del formulario:", request.POST)

        if libro_form.is_valid():
            try:
                libro_form.save()
                return redirect('index')
            except Exception as e:
                print(f"Error al guardar el libro: {e}")
                libro_form.add_error(None, "Error al guardar el libro.")
        else:
            print("Errores de validación:", libro_form.errors)  

        
        if not libro_form.is_valid():
            print("Errores de validación después de intentar guardar:", libro_form.errors)

    else:
        libro_form = LibroForm()

    return render(request, 'agregar_libro.html', {
        'libro_form': libro_form,
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

def obtener_carrito(request):
    carrito_data = request.session.get('carrito', None)
    if carrito_data is None:
        return Carrito()  
    return Carrito(carrito_data) 



def guardar_carrito(request, carrito):
    
    request.session['carrito'] = carrito.serializar()
    request.session.modified = True

def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito = obtener_carrito(request)
    
    
    
    try:
        if libro.stock > 0:
            carrito.agregar_articulos(libro, 1)
            guardar_carrito(request, carrito)
            messages.success(request, f"{libro.titulo} agregado al carrito.")
        else:
            messages.error(request, 'No hay stock disponible de este libro.')
    except ValueError as e:
        messages.error(request, str(e))
        
    return redirect('detalles_libro', libro_id=libro_id)

def ver_carrito(request):
    carrito = obtener_carrito(request)
    total = carrito.calcular_total()  
    return render(request, 'carrito.html', {'carrito': carrito.articulos, 'total': total})

def vaciar_carrito(request):
    carrito_data = request.session.get('carrito', {})
    
    if carrito_data:
        for item in carrito_data.get('articulos', []):
            libro_id = item['libro_id']
            cantidad = item['cantidad']
            
            
            libro = get_object_or_404(Libro, id=libro_id)
            libro.incrementar_stock(cantidad)
        
        del request.session['carrito']
        messages.success(request, "El carrito ha sido vaciado y el stock ha sido restaurado.")
    else:
        messages.warning(request, "El carrito ya está vacío.")
    
    return redirect('carrito')