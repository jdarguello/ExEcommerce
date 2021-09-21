from rest_framework import serializers

from cheackout1130619212.models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class InfoSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'
