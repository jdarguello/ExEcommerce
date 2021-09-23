from django.db import models
from django.db.models.fields import BooleanField
from Productos.models  import Producto 


# Create your models here.
class CarritoCompras(models.Model):
    usuario =  models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False) 
    #(null=True, blank=True)


    def __str__(self):
        return self.usuario


    def total(self):
        pass
    
    def numArt(self):
        pass 

    
class Articulo(models.Model):
      carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
      producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
      cantidad = models.IntegerField()

      # def tipoEl(self):
      #    from Productos.serializers import TipoSerial
      
      def __str__(self):
        return self.carrito+" - "+self.producto.nombre  
     
     
      def subtotal(self):
          pass
    

class infoEnvio(models.Model):
     carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
     nombre = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     direccion = models.CharField(max_length=300)
     paais = models.CharField(max_length=300)
     departamento = models.CharField(max_length=300)
     ciudad = models.CharField(max_length=300)

     def __str__(self):
        return self.nombre 
   