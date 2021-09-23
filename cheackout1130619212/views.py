from django.http.response import Http404
from django.shortcuts import render
from rest_framework.status import HTTP_400_BAD_REQUEST

from rest_framework import viewsets
from rest_framework.response import Response

from cheackout1130619212.models import *

from cheackout1130619212.serializador import *

class CarritoAPI (viewsets.ModelViewSet):
    serializer_class = CarritoSerial
    queryset = CarritoCompras.objects.all()

class ArticuloAPI (viewsets.ViewSet):
    def list (self, request):
        articulos=Articulo.objects.all()
        serializar = ArticuloSerial(articulos, many=True)
        return Response(serializar.data)

    def create(self,request):
        serial=ArticuloSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response ({'Creados':True})
        return Response(serial.errors, HTTP_400_BAD_REQUEST)


class InfoAPI (viewsets.ModelViewSet):
    serializer_class = InfoSerial
    queryset = InfoEnvio.objects.all()


