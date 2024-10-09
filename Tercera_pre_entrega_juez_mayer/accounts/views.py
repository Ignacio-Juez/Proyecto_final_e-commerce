from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserProfileForm,  CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

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
        profile_form = UserProfileForm(request.POST, instance=user)
        password_form = CustomPasswordChangeForm(user=user, data=request.POST)  
        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  
            return redirect('index')  

    else:
        profile_form = UserProfileForm(instance=user)
        password_form = CustomPasswordChangeForm(user=user)  

    return render(request, 'edit_profile.html', {
        'form': profile_form,
        'password_form': password_form,  
    })