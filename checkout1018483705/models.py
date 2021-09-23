import re
from django.db import models
from Productos.models import *
# Create your models here.

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario

    def total(self):
        arts = self.articulo_set.all()
        total = 0
        for art in arts:
            total += art.subtotal()
        
        return total

    def numArticulo(self):
        arts = self.articulo_set.all()
        return len(arts)


class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        #return self.nombre+" "+ self.apellido
        return self.carrito.__str__()


class Articulo (models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.usuario + " " + self.producto.nombre

    def subtotal(self):
        ## Here 
        return self.producto.precio * self.cantidad
