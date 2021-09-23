#from django.shortcuts import render

# Create your views here.
from checkout1098681166_1.models import CarritoCompras
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

# Create your views here.

from .serializers import *

#----------------------------------CARRITO---------------------------------------#

class CarritoComprasAPI(viewsets.ViewSet):
    def list(self, request):
        #request => peticiones de usuario
        #List => cumple el objetivo de listar una serie de registros en la DB
        carritos = CarritoCompras.objects.all()
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create(self, request):
        #Crear registros en la DB
        #nuevoCarrito = CarritoCompras.objects.create(usuario=request.data["usuario"])
        serialCarrito = CarritoSerial(data=request.data)
        if serialCarrito.is_valid():
            serialCarrito.save()
            return Response({"Exito":True})
        return Response(serialCarrito.errors)
        
    def retrieve(self, request, pk=None):
        #pk => identificar y obtener objetos
        #retrieve => obtener informacion de uno o varios objetos a partir de la info enviada en la url
        carritosUsuario = CarritoCompras.objects.filter(usuario=pk) # filter muchos objetos
        carritoS = CarritoSerial(carritosUsuario, many=True)
        return(pk)

#--------------------------------ARTICULO--------------------------------------------#

class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        #request => peticiones de usuario
        #List => cumple el objetivo de listar una serie de registros en la DB
        articulos = Articulo.objects.all()
        serializador = ArticuloSerial(articulos, many=True)
        return Response(serializador.data)

    def create(self, request):
        #Crear registros en la DB
        #nuevoCarrito = CarritoCompras.objects.create(usuario=request.data["usuario"])
        serialArticulo = ArticuloSerial(data=request.data)
        if serialArticulo.is_valid():
            serialArticulo.save()
            return Response({"Exito": True})
        return Response(serialArticulo.errors)

    def retrieve(self, request, pk=None):
        #pk => identificar y obtener objetos
        #retrieve => obtener informacion de uno o varios objetos a partir de la info enviada en la url
        articuloUsuario = Articulo.objects.get(pk=pk)  # filter muchos objetos
        articuloS = ArticuloSerial(articuloUsuario)
        return Response(articuloS.data)

#--------------------------------INFO ENVIO--------------------------------------------#


class InfoAPI(viewsets.ViewSet):
    def list(self, request):
        #request => peticiones de usuario
        #List => cumple el objetivo de listar una serie de registros en la DB
        envios = InfoEnvio.objects.all()
        serializador = InfoSerial(envios, many=True)
        return Response(serializador.data)

    def create(self, request):
        #Crear registros en la DB
        #nuevoCarrito = CarritoCompras.objects.create(usuario=request.data["usuario"])
        serialEnvio = InfoSerial(data=request.data)
        if serialEnvio.is_valid():
            serialEnvio.save()
            return Response({"Exito": True})
        return Response(serialEnvio.errors)

    def retrieve(self, request, pk=None):
        #pk => identificar y obtener objetos
        #retrieve => obtener informacion de uno o varios objetos a partir de la info enviada en la url
        envioUsuario = Articulo.objects.filter(usuario=pk)  # filter muchos objetos
        envioS = InfoSerial(envioUsuario, many=True)
        return Response(pk)
