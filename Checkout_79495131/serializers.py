from rest_framework import serializers

from .models import CarritoCompra, InfoEnvio, Articulo

from Checkout_79495131.models import CarritoCompra


class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompra
        fields = '__all__'


class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'


class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
