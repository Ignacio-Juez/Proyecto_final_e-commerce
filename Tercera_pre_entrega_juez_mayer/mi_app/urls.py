from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),   
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('gestionar_libros/', views.gestionar_libros, name='gestionar_libros'),
    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('detalles_libro/<int:libro_id>/', views.detalles_libro, name='detalles_libro'),
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name = "eliminar_libro"),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('agregar_al_carrito/<int:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
