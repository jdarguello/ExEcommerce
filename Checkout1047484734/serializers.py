from Checkout1047484734.models import *
from rest_framework import serializers
from Productos.models import *

class CarritoComprasSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'
        
class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ["carrito", "producto", "cantidad"]