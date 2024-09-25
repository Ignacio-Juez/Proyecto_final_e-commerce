Tercera Pre-Entrega Juez Mayer

Pasos para testear mi proyecto:
1. Clonar el repositorio.
2. Activar el entorno virtual.
3. Ejecutar 'python manage.py migrate'.
4. Ejecutar 'python manage.py runserver'.

Orden para probar las funcionalidades:
1. Iniciar el servidor.
2. Ir a http://127.0.0.1:8000/ .
3. Tocar el boton "Agregar Libro" o ingresar a la url http://127.0.0.1:8000/agregar_libro/ . Llenar todos los campos y apretar guardar.
4. Tocar el boton "Buscar Libro" o ingresar a la url http://127.0.0.1:8000/buscar_libro/ colocar el titulo completo o parcial del titulo solicitado.

Funcionalidades (lectura opcional):
 Atento a las recomendaciones dadas por el profesor Mauricio en la clase 21, usare gran parte de esta pre-entrega para mi proyecto final, por lo que no todas
las funcionalidades de la plantilla que descargue de https://html.design/download/memorial-library-html-template/ estan terminadas. Sin embargo, los requisitos
de esta pre-entrega estan satisfechos en los siguientes puntos:
 
-Herencia de HTML: Las plantillas agregar_libro.html y buscar_libro.html heredan de la plantilla base index.html.
-Modelos: Mis modelos son Libro, Autor y Editorial.
-Formularios: Formularios para agregar y buscar libros utilizando los modelos.
-Búsqueda: Tengo un formulario de búsqueda de libros.

Futuros desafios para el proyecto final (lectura opcional): 
    -Como bien me respondio el profesor Mauricio en la clase 22 en un e-commerce lo ideal es que las personas que puedan modificar y agregar elementos tengan algun tipo de permiso de administrador.
    -Agregar funcionalidades al boton About US y revisar el boton de Contact Us. En el boton de perfil permitirle al usuario loguearse y tener un carrito con sus compras.
    -Agregar un elemento de stock en los libros y que cuando se vuelva 0 el cliente ya no pueda comprar.
    -Dejar la lupa a modo estetico con la funcionalidad de buscar libros y eliminar el otro boton.
    -Darle funcionalidad a los botones de redes sociales.
    -Entre otros

