from django.db import models
from django.contrib.auth import get_user_model
#SE DEDE IMPORTAR LA CLASE PRODUCTO
# PORQUE ASI LO INDICA EL MODELO UML

from Productos.models import Producto

class CarritoCompras(models.Model):
#ATRIBUTOS
    usuario = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    dcto= models.FloatField(default=0)
    cantMinima= models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

#METODOS

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)

    @property
    def total(self):
        total=0
        articulos = Articulo.objects.filter(carrito=self)
        for articulo in articulos:
            total += articulo.subtotal()
        return total



    def numArt(self):
        articulos= Articulo.objects.filter(carrito=self)
        return len(articulos)

class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombres= models.CharField(max_length=200)
    apellidos= models.CharField(max_length=200)
    direccion= models.CharField(max_length=200)
    pais= models.CharField(max_length=200)
    departamento= models.CharField(max_length=200)
    ciudad= models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True) #Se hace esta confifiguracicion porque es una relacion tio asociacion
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.__str__()

    def subtotal(self):
#Subtotal = precioUnitario*Cantidad
        return self.producto.precio * self.cantidad