from Productos.models import Producto
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from Productos.models import Producto


class carritoCompras (models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = BooleanField(default=False)

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)
    
    def total(self):
        total = 0
        articulos = articulo.objects.filter(carrito=self) #obtiene los registrados para este carrito
        for articulos in articulos:
            total += articulo.subtotal()
        return total


    def numArt (self):
        articulos = articulo.objects.filter(carrito=self)
        return len(articulos)
        

class infoEnvio (models.Model):
    carrito = models.ForeignKey(carritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()

class articulo (models.Model):
    carrito = models.ForeignKey(carritoCompras, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " / " + self.Producto.__str__()

    def subtotal(self):
        #subtotal = precioUnitario*cantidad
        return self.Producto.precio*self.cantidad





 

