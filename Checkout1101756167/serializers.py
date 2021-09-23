from rest_framework import serializers

from .models import *

class CarritoComprasSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'
        #fields = ["nombre", "foto"]

class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'


class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'