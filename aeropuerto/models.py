from django.db import models

# Create your models here.

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Ruta(models.Model):
    origen = models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')
    destino = models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')