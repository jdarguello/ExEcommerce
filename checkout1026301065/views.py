from django.shortcuts import render
from rest_framework import viewsets
from checkout1026301065.models import *
from checkout1026301065.serializers import *

class CarritoCompraAPI(viewsets.ModelViewSet):
    serializers_class=CaritoSerial
    queryset= CarritoCompras.objects.all()
class ArticuloAPI(viewsets.ModelViewSet):
    serializers_class=ArticuloSerial
    queryset= Articulo.objects.all()
class InfoEnvioAPI(viewsets.ModelViewSet):
    serializers_class=InfoEnvioSerial
    queryset= InfoEnvio.objects.all()