from django.shortcuts import render

# Create your views here.

# APIS
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

# Creación de las APIS

# from Checkout_1095834454.serializers import *
from .serializers import *

class CarritoAPI(viewsets.ViewSet):
    def list(self, request):
        # request => Se trata de la petición de usuario => GET, POST, PUT...
        carritos = CarritoCompras.objects.all()
        carritoSerializador = CarritoComprasSerial(carritos, many=True)
        return Response(carritoSerializador.data)
    
    def create(self, request):
        # Crear nuevos elementos en la base de datos
        # serializer = CarritoComprasSerial(data=request.data, many=True)
        nuevoCarritoSerial = CarritoComprasSerial(data=request.data)
        if nuevoCarritoSerial.is_valid():
            nuevoCarritoSerial.save()
            return Response({"Exito":True})
        return Response(nuevoCarritoSerial.errors)
    
    def retrieve(self, request, pk=None):
        # Obtener uno o varios objetos de la base de datos
        # pk => Llave primaria - método de identificación de nuestros objetos
        carrito = CarritoCompras.objects.get(pk=pk)
        serializador = CarritoComprasSerial(carrito)
        
        return Response(serializador.data)
    
    def partial_update(self, request, pk=None):
        # Permite actualizar atributos de los objetos CRUD
        carrito = CarritoCompras.objects.get(pk=pk)
        carritoS = CarritoComprasSerial(carrito, request.data, partial=True)
        if carritoS.is_valid():
            carritoS.save()
            return Response({"Actualizado":True})
        return Response(carritoS.errors)
    
    def update(self, request):
        # Permite actualizar TODOS los argumentos en la base de datos
        carrito = CarritoCompras.objects.get(pk=pk)
        carritoS = CarritoComprasSerial(carrito, request.data, partial=True)
        if carritoS.is_valid():
            carritoS.save()
            return Response({"Actualizado":True})
        return Response(carritoS.errors)
    
    def destroy(self, request, pk=None):
        # Permite borrar un objeto de la base de datos
        carrito = CarritoCompras.objects.get(pk=pk)
        carrito.delet()
        return Response({"Delete":True})
    
        

class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        articulosSerializador = ArticuloSerial(articulos, many=True)
        
        return Response(articulosSerializador.data)
    
    def create(self, request):
        nuevoArticuloSerial = ArticuloSerial(data=request.data)
        if nuevoArticuloSerial.is_valid():
            nuevoArticuloSerial.save()
            return Response({"Exito":True})
        
        return Response(nuevoArticuloSerial.errors)
    
    def retrieve(self, request, pk=None):
        articulo = Articulo.objects.get(pk=pk)
        serializador = ArticuloSerial(articulo)
        
        return Response(serializador.data)
    
class InfoEnvioAPI(viewsets.ViewSet):
    def list(self, request):
        informacionEnvio = InfoEnvio.objects.all()
        informacionSerializador = InfoEnvioSerial(informacionEnvio, many=True)
        
        return Response(informacionSerializador.data)
    
    def create(self, request):
        nuevoInformacionSerial = InfoEnvioSerial(data=request.data)
        if nuevoInformacionSerial.is_valid():
            nuevoInformacionSerial.save()
            return Response({"Exito":True})
        return Response(nuevoInformacionSerial.errors)
    
    def retrieve(self, request, pk=None):
        infoEnvio = InfoEnvio.objects.get(pk=pk)
        serializador = InfoEnvioSerial(infoEnvio)
        
        return Response(serializador.data)
