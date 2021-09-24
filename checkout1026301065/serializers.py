from rest_framework import serializers
from checkout1026301065.models import *


class CaritoSerial(serializers.ModelSerializer):
    	class Meta:
            model = CarritoCompras
            fields = ['usuario', 'fecha', 'total']
class ArticuloSerial(serializers.ModelSerializer):
    	class Meta:
            model = Articulo
            fields = '__all__'
class InfoEnvioSerial(serializers.ModelSerializer):
    	class Meta:
            model = InfoEnvio
            fields = '__all__'        
        