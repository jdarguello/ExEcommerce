from Productos.models import *
from django.db import models

class CarritoCompras (models.Model):
    usuario = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.usuario + " - " + str(self.fecha)

    def total(self):
        pass

    def numArt(self):
        pass

class InfoEnvio (models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.carrito.__str__()

class Articulo (models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + "/" + self.producto.__str__()

    def subtotal(self):
        pass
