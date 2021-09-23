from django.db.models import fields
from checkout31.models import *
from rest_framework import serializers

class carrito_compras_serial (serializers.ModelSerializer):
    class Meta:
        model= carrito_compras
        #fields = ["usuario","fecha","pagado"]
        fields = '__all__'

class articulo_serial (serializers.ModelSerializer):
    class Meta:
        model= articulo
        #fields = ["carrito","producto","cantidad"]
        fields = '__all__'

class info_envio_serial (serializers.ModelSerializer):
    class Meta:
        model= info_envio
        #fields = ["ciudad","direccion"]
        fields = '__all__'