#Creamos los serializadores de nuestra aplicaci�n

#Serializadores => convertir en diccionarios Python
# los objetos CRUD

from rest_framework import serializers

from checkout_72186587.models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras 
        fields = '__all__'
        #fields = ["nombre", "foto"]


class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
        #fields = ["nombre", "precio", "descripcion", "marca", "ref", "tipoEl"]


class InfoSerial(serializers.ModelSerializer):
    class Meta:
        model = infoEnvio 
        fields = '__all__'
        