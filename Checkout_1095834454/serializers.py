from django.core import exceptions
from rest_framework import serializers
# from Checkout_1095834454.models import *
from .models import *   # Funciona para importar dentro de la misma aplicación (Checkout...)

class CarritoComprasSerial(serializers.ModelSerializer):
    class Meta:
         model = CarritoCompras
         fields = "__all__"

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
         model = Articulo
         fields = "__all__"

class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
         model = InfoEnvio
         fields = "__all__"
