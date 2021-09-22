from rest_framework import serializers

from .models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'

class InfoSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'