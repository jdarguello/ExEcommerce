from django.db.models import fields
from django.utils.translation import deactivate
from checkout1018483705.models import *
from rest_framework import serializers

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