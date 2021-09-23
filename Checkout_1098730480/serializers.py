from rest_framework import serializers

from .models import *   #=> from Checkout_1098349.models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'
