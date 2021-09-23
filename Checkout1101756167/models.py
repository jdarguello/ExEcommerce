from django.db import models
from django.contrib.auth import get_user_model

from Productos.models import Producto

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True) #16/09/2021
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario) + " - " + str(self.fecha)

    @property
    def total(self):
        total = 0
        for articulo in self.articulo_set.all():
            total += articulo.subtotal()
        return total
    
    def numArt(self):
        articulos = Articulo.objects.filter(carrito=self)
        return len (articulos)

class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)
    

    def __str__(self):
        return self.carrito.__str__() + " - " +  self.Producto.__str__() 
    
    def subtotal(self):
        #subtotal = precioUNitario*cantidad
        return self.producto.precio*self.cantidad
    
    