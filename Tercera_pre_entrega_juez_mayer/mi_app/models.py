# Create your models here.
from decimal import Decimal
from django.db import models
from django.shortcuts import get_object_or_404

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
    
class Carrito:
    def __init__(self, carrito_data=None):
        self.articulos = []
        if carrito_data:
            
            for item in carrito_data.get('articulos', []):
                libro = get_object_or_404(Libro, id=item['libro_id'])
                self.articulos.append({
                    "libro": libro, 
                    "precio": item['precio'],
                    "cantidad": item['cantidad']
                })

    def agregar_articulos(self, libro, cantidad):
        if libro.stock >= cantidad:
            self.articulos.append({
                "libro": libro, 
                "precio": float(libro.precio),  
                "cantidad": cantidad
            })
        
            libro.stock -= cantidad
            libro.save()
        else:
            raise ValueError(f"No hay suficiente stock para {libro.titulo}")

    def remover_articulo(self, libro):
        for item in self.articulos:
            if item["libro"] == libro:
                self.articulos.remove(item)
                break

    def calcular_total(self):
        total = 0.00
        for item in self.articulos:
            total += item["precio"] * item["cantidad"]
        return total

    def serializar(self):
        
        return {
            "articulos": [
                {
                    "libro_id": item["libro"].id,  
                    "precio": item["precio"],       
                    "cantidad": item["cantidad"],
                } for item in self.articulos
            ]
        }
