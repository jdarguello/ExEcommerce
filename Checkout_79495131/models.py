from Productos.models import Producto
from django.db import models

class CarritoCompra(models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario + '-' + str(self.fecha)

    def total(self) -> float:
        pass

    def numArt(self) -> int:
        pass



class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.carrito.__str__()

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + '-' + self.producto.__str__()

    def subtotal(self) -> float:
        return self.cantidad * self.producto.precio