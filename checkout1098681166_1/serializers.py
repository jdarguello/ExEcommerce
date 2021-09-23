from django.db.models import fields
from rest_framework import serializers


from checkout1098681166_1.models import *

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
