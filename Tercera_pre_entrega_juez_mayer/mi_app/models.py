# Create your models here.

from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True, null=False, blank=False, default="0000000000000")
    fecha_publicacion = models.DateField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    imagen_url = models.URLField(max_length=500, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def incrementar_stock(self, cantidad):
        self.stock += cantidad
        self.save()

    def reducir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
        else:
            raise ValueError("Stock insuficiente")

    def __str__(self):
        return f"{self.titulo} ({self.stock} en stock)"

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
