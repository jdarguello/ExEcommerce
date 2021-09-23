from functools import partial
from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from rest_framework.response import Response 
from .serializer import * 
from django.shortcuts import get_object_or_404


# Create your views here.

class CarritoApi(viewsets.ViewSet):
    def list(self, request):
        carritos = CarritoCompras.objects.all()
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create(self, request):
       # nuevoCarrito  = CarritoCompras.objects.create(usuario=request.data["usuario"]) 
        serializador = CarritoSerial(data=request.data)
        if serializador.is_valid:
            serializador.save()
            return Response({"Exito":True})
        return Response(serializador.errors)

    def retrieve(self, request, pk=None):
        #obtner un solo registro de la base de datos
        #pk es primari key 
        #carrito = CarritoCompras.objects.get(id=pk)
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        serializador = CarritoSerial(carrito)
        return Response(serializador.data)

    def partial_update(self, request, pk=None):
        # se actualización parcial con el PATCH
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        carritoS = CarritoSerial(carrito, request.data, partial=True)
        if carritoS.is_valid():
            carritoS.save 
            return Response("Actualizado")
        return Response(carritoS.errors)
         

    def update(self, request, pk=None):
        # se actualización parcial con el PUT
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        carritoS = CarritoSerial(carrito, request.data)
        if carritoS.is_valid():
            carritoS.save 
            return Response("Actualizado")
        return Response(carritoS.errors)

    def destroy(self, request, pk=None):
        carrito = CarritoCompras.objects.get(id = pk)
        carrito.delete()
        return response("Objeto borrado", True)



class ArticuloApi(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializador = ArticuloSerial(articulos, many=True)
        return Response(serializador.data)

    def create(self, request):
       # nuevoCarrito  = CarritoCompras.objects.create(usuario=request.data["usuario"]) 
        serializador = ArticuloSerial(data=request.data)
        if serializador.is_valid:
            serializador.save()
            return Response({"Exito":True})
        return Response(serializador.errors)

    def retrieve(self, request, pk=None):
        #obtner un solo registro de la base de datos
        #pk es primari key 
        articulos = get_object_or_404(CarritoCompras, pk=pk)
        serializador = ArticuloSerial()
        return Response(pk)

class InfoEnvioApi(viewsets.ViewSet):
    def list(self, request):
        info = infoEnvio.objects.all()
        serializador = InfoSerial(info, many=True)
        return Response(serializador.data)

    def create(self, request):
       # nuevoCarrito  = CarritoCompras.objects.create(usuario=request.data["usuario"]) 
        serializador = InfoSerial(data=request.data)
        if serializador.is_valid:
            serializador.save()
            return Response({"Exito":True})
        return Response(serializador.errors)

    def retrieve(self, request, pk=None):
        #obtner un solo registro de la base de datos
        #pk es primari key 
        info = get_object_or_404(CarritoCompras, pk=pk)
        serializador = ArticuloSerial()
        return Response(pk)