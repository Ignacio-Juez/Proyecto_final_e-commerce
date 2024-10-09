from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required

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

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página que desees después de guardar
    else:
        form = UserProfileForm(instance=user)  # Rellena el formulario con la información actual del usuario

    return render(request, 'edit_profile.html', {'form': form})

