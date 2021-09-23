from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField

from Productos.models import Producto

class carrito_compras (models.Model):
    usuario = models.CharField(max_length=20,null = False)
    fecha = models.DateField(auto_now_add = True)
    dcto = models.FloatField(null = True, blank = True)
    cantminima = models.IntegerField (null = True, blank = True)
    pagado = models.BooleanField(default=False)

    def __str__ (self):
        return self.usuario + "(" + str(self.fecha) +")"
    
    def total (self):
        pass
    def num_art (self):
        pass

class articulo (models.Model):
    carrito = models.ForeignKey(carrito_compras, on_delete=models.CASCADE, null = False)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True)
    cantidad = models.IntegerField(default=0)

    def __str__ (self):
        return self.carrito.usuario + "(" + self.producto.nombre + ")"

    def subtotal (self):
        return self.cantidad * self.producto.precio

class info_envio (models.Model):
    carrito = models.ForeignKey(carrito_compras, on_delete=models.CASCADE, null = False)
    nombre = models.CharField(max_length= 200,null = False)
    apellido = models.CharField(max_length= 200,null = False)
    pais = models.CharField(max_length= 200,null = False)
    departamento = models.CharField(max_length= 200,null = False)
    ciudad = models.CharField(max_length= 200,null = False)
    direccion = models.CharField(max_length= 200,null = False)
 
    def __str__ (self):
        return self.carrito.usuario + "(" + self.nombre + "-" +self.direccion + ")"