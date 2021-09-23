from Productos.models import Producto
from django.db import models

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True) #16/09/2021
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)
    
    def total(self):
        total = 0
        articulos = Articulo.objects.filter(carrito=self)
        for articulo in articulos:
            total +=articulo.subtotal()            

    def numArt(self):
        articulos =Articulo.objects.filter(carrito=self)
        return len(articulos)


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
        return self.carrito.__str__() + "/" + self.producto.__str__()

    def subtotal(self):
        return self.producto.precio * self.cantidad
