from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import *

class CarritoComprasAPI (viewsets.ViewSet):
    def list(self, request):
        carritos = CarritoCompras.objects.all()
        serializador = CarritoSerial(carritos,many=True)
        return Response(serializador.data)

    def create(self,request):
        serialCarrito = CarritoSerial(data=request.data)
        if serialCarrito.is_valid():
            serialCarrito.save()
            return Response({"Exito": True})
        return Response(serialCarrito.errors)

    def retrieve(self, request, pk=None):
        #pk => primary key -> es decir: argumento que permite identificar y obtener objetos
        #retrieve => enviar la información de uno o varios objetos
        carritosUsuario = CarritoCompras.objects.filter(usuario=pk)
        carritoS = CarritoSerial(carritosUsuario, many=True)
        return Response(carritoS.data)




class InfoEnvioAPI (viewsets.ViewSet):
    def list(self, request):
        infoenvios = InfoEnvio.objects.all()
        serializador = InfoSerial(infoenvios,many=True)
        return Response(serializador.data)

    def create(self, request):
        serialInfoEnv = InfoSerial(data = request.data)
        if serialInfoEnv.is_valid():
            serialInfoEnv.save()
            return Response({"InfoEnv":"created"})
        return Response(serialInfoEnv.errors)

    def retrieve(self, request, pk=None):
        InfoEnvUsr = InfoEnvio.objects.filter(usuario=pk)
        infoEnvioS = InfoSerial(InfoEnvUsr,many=True)
        return Response(infoEnvioS.data)



class ArticuloAPI (viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializador = ArticuloSerial(articulos,many=True)
        return Response(serializador.data)

    def create(self,request):
        serialArt = ArticuloSerial(data = request.data)
        if serialArt.is_valid():
            serialArt.save()
            return Response({"Articulo":" created"})
        return Response(serialArt.errors)

    def retrieve(self, request, pk=None):
        articulos = Articulo.objects.get(pk=pk)
        articuloS = ArticuloSerial(articulos)
        return Response(articuloS.data)

    def partial_update(self, request,pk=None):
        artModificar = Articulo.objects.get(pk=pk)
        serializador = ArticuloSerial(artModificar,request.data, partial=True)
        if serializador.is_valid():
            serializador.save()
            return Response({"Actualizado":True})
        return Response(serializador.errors)