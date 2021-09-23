from django.db import models
from django.db.models.aggregates import Max
from Productos.models import Producto
# Create your models here.


class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)

    def total(self):
        total = 0
        #articulos = Articulo.objects.all()      #=> Trae TODOS los artículos de base de datos
        # => Obtiene los registrados para este carrito
        articulos = Articulo.objects.filter(carrito=self)
        for articulo in articulos:
            total += articulo.subtotal()
        return total

    def numArt(self):
        articulos = Articulo.objects.filter(carrito=self)
        return len(articulos)


class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.__str__()

    def subtotal(self):
        return self.producto.precio*self.cantidad


class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()
