from .models import * 
from rest_framework import serializers

class CarritoComprasSerial(serializers.ModelSerializer):
    class Meta :
        model = CarritoCompras
        fields ='__all__'

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class InfoSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'