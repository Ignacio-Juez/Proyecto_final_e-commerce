from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm 
def register(request):
     
    if request.method == 'POST':
         
        form = UserRegisterForm(request.POST)
        if form.is_valid():
             
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {"mensaje": "Usuario Creado :"})
          

    else:
        
        form = UserRegisterForm()
    
    return render(request, "register.html", {"form": form})

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data =  request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)

                return render(request, "/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:

                return render(request, "/index.html", {"mensaje": "Error, datos incorrectos"})
            
        else:

            return render(request, "index.html", {"mensaje": "Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "login.html", {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return redirect('login')

