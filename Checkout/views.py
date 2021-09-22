from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *

# Create your views here.

class CarritoAPI(viewsets.ViewSet):
    def list(self, request):
        #Listar Informacion
        #request => peticion de usuarios. GET, POST, PUT, ...
        carritos = CarritoCompras.objects.all()
        serializador = CarritoSerial(carritos, many = True)
        return Response(serializador.data)


    def create(self, request):
        # Crear registros en bases de datos
        #nuevoCarrito = CarritoCompras.objects.create(usuario=request.data["usuario"])
        serializador = CarritoSerial(data=request.data)
        if serializador.is_valid():
            serializador.save() #Grauda el nuevo objeto
            return Response({"Exito":True}) #Creo el objeto
        return Response(serializador.errors)


    def retrieve(self, request, pk=None):
        #Obtener un solo registro de la base de datos
        #pk => Primary key
        carrito = get_object_or_404(CarritoCompras, pk = pk)
        serializador = CarritoSerial(carrito)
        return Response(serializador.data)

    def partial_update(self, request, pk=None):
        #Actualización parcial => PATCH
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        carritoS = CarritoSerial(carrito, request.data, partial=True)
        if carritoS.is_valid():
            carritoS.save()
            return Response("Actualizado")
        return Response(carritoS.errors)

    def update(self, request, pk=None):
        #Actualiza registros => PUT
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        carritoS = CarritoSerial(carrito, request.data)
        if carritoS.is_valid():
            carritoS.save()
            return Response("Actualizado")
        return Response(carritoS.errors)
        
    
    def destroy(self, request, pk=None):
        #borramos elementos en base de datos
        carrito = CarritoCompras.objects.get(id=pk)
        carrito.delete()
        return Response({"Objeto borrado":True})

class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        #Listar Informacion
        #request => peticion de usuarios. GET, POST, PUT, ...
        articulo = Articulo.objects.all()
        serializador = ArticuloSerial(articulo, many = True)
        return Response(serializador.data)

    def create(self, request):
        # Crear registros en bases de datos
        serializador = ArticuloAPI(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({"Exito":True})
        return Response(serializador.errors)

    def retrieve(self, request, pk=None):
        #Obtener un solo registro de la base de datos
        #pk => Primary key
        articulo = get_object_or_404(Articulo, pk=pk)
        serializador = ArticuloSerial(articulo)
        return Response(serializador.data)

    def partial_update(self, request, pk=None):
        #Actualización parcial => PATCH
        carrito = get_object_or_404(Articulo, pk=pk)
        articuloS = ArticuloSerial(Articulo, request.data, partial=True)
        if articuloS.is_valid():
            articuloS.save()
            return Response("Actualizado")
        return Response(articuloS.errors)

    def update(self, request, pk=None):
        #Actualiza registros => PUT
        articulo = get_object_or_404(Articulo, pk=pk)
        articuloS = ArticuloSerial(articulo, request.data)
        if articuloS.is_valid():
            articuloS.save()
            return Response("Actualizado")
        return Response(articuloS.errors)
        
    def destroy(self, request, pk=None):
        #borramos elementos en base de datos
        articulo = Articulo.objects.get(id=pk)
        articulo.delete()
        return Response({"Objeto borrado":True})

class InfoEnvioAPI(viewsets.ViewSet):
    def list(self, request):
        #Listar Informacion
        #request => peticion de usuarios. GET, POST, PUT, ...
        infoEnvio = InfoEnvio.objects.all()
        serializador = InfoEnvioSerial(infoEnvio, many = True)
        return Response(serializador.data)

    def create(self, request):
        # Crear registros en bases de datos
        serializador = InfoEnvioAPI(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({"Exito":True})
        return Response(serializador.errors)

    def retrieve(self, request, pk=None):
        #Obtener un solo registro de la base de datos
        #pk => Primary key
        infoenvio = get_object_or_404(InfoEnvio, pk=pk)
        serializador = InfoEnvioSerial(InfoEnvio)
        return Response(serializador.data)

    def partial_update(self, request, pk=None):
        #Actualización parcial => PATCH
        infoEnvio = get_object_or_404(InfoEnvio, pk=pk)
        infoEnvioS = InfoEnvioSerial(infoEnvio, request.data, partial=True)
        if infoEnvioS.is_valid():
            infoEnvioS.save()
            return Response("Actualizado")
        return Response(infoEnvioS.errors)

    def update(self, request, pk=None):
        #Actualiza registros => PUT
        infoEnvio = get_object_or_404(InfoEnvio, pk=pk)
        infoEnvioS = InfoEnvioSerial(infoEnvio, request.data)
        if infoEnvioS.is_valid():
            infoEnvioS.save()
            return Response("Actualizado")
        return Response(infoEnvioS.errors)
    
    def destroy(self, request, pk=None):
        #borramos elementos en base de datos
        infoEnvio = InfoEnvio.objects.get(id=pk)
        infoEnvio.delete()
        return Response({"Objeto borrado":True})