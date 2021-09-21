from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from Productos.models import *



class CarritoCompras (models.Model):
    usuario = CharField(max_length=200,null=True,blank=True)
    fecha = DateField(auto_now_add=True)
    descuento = FloatField(max_length=7,null=True,blank=True)
    CantMinima = IntegerField(max_length=7,null=True,blank=True)
    pagado = BooleanField()

    def total():
        pass
    def __str__(self):
        return self.usuario
    def numArt():
        pass

class Articulo(models.Model):
    carrito = ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = IntegerField(max_length=7,null=True,blank=True)

    def __str__(self):
        return self.carrito
    
    def subtotal():
        pass
    
class InfoEnvio(models.Model):
    carrito = ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = CharField(max_length=200,null=True,blank=True)
    apellido = CharField(max_length=300,blank=True,null=True)
    direccion = CharField(max_length=300,blank=True,null=True)
    pais = CharField(max_length=300,blank=True,null=True)
    departamento = CharField(max_length=300,blank=True,null=True)
    ciudad = CharField(max_length=300,blank=True,null=True)
    
    def __str__(self):
        return self.nombre


# Create your models here.
