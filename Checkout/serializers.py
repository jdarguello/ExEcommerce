from django.db.models import fields
from rest_framework import serializers

from .models import * # => from checkout.models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model= CarritoCompras
        fields = '__all__'

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'