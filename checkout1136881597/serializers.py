from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = carritoCompras
        fields = '__all__'
    
class InfoSerial(serializers.ModelSerializer):
    class Meta:
        model = infoEnvio
        fields = '__all__'

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = articulo
        fields = '__all__'



