from django.db import models
from Productos.models import *

# Create your models here.
class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.usuario} - {self.fecha}"
    
    def total(self):
        
        pass
    
    def numArticulos(self):
        pass

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.carrito.__str__()} / {self.producto.nombre}"
    
    def subtotal(self):
        subtotal = 0
        subtotal += self.producto.precio * self.cantidad
        return subtotal

class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.carrito.__str__()
    
        