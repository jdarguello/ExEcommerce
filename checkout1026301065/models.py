import Productos
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

from Productos.models import *

'''class CarritoCompras(models.Model):
    #dvariables
    usurio=models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    fecha=models.DateField(auto_now_add=True)
    descuento=models.FloatField(null=True)
    cantMinima = models.IntegerField()
    pagado=models.BooleanField(default=False)
    #metodos
    def __str__(self):
        return str(self.usuario) + " - " + str(self.fecha)
    def total(self):
        total=0
        for articulo in self.articulo_set.all():
            total += articulo.subtotal()
        return total'''
class CarritoCompras(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario) + " - " + str(self.fecha)

    @property
    def total(self):
        total = 0
        for articulo in self.articulo_set.all():
            total += articulo.subtotal()
        return total

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.nombre
    
    def subtotal(self):
        return self.producto.precio*self.cantidad
class InfoEnvio(models.Model):
    carrito=models.ForeignKey(CarritoCompras,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    direccion=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    departamento=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)

    def __str__(self):
        return self.carrito.__str__()




