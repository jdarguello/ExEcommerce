from django.db import models

from Productos.models import Producto

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.FloatField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)   #Ejemplo: juand - 21/09/2021
    
    def total(self):
        pass

    def numArt(self):
        pass

class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        #self.carrito => objeto del tipo 'CarritoCompras'
        return self.carrito.__str__()   #self.carrito.usuario + " - " + self.carrito.fecha

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.__str__()
    
    def subtotal(self): 
        #subtotal = precioUnitario*cantidad
        return self.cantidad*self.producto.precio
