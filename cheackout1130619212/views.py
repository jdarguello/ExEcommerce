from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from cheackout1130619212.models import *

from cheackout1130619212.serializador import *

class CarritoAPI (viewsets.ModelViewSet):
    serializer_class = CarritoSerial
    queryset = CarritoCompras.objects.all()

class ArticuloAPI (viewsets.ModelViewSet):
    serializer_class = ArticuloSerial
    queryset = Articulo.objects.all()

class InfoAPI (viewsets.ModelViewSet):
    serializer_class = InfoSerial
    queryset = InfoEnvio.objects.all()


