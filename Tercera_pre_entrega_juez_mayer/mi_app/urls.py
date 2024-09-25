from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),   
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
]
