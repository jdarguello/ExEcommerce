from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from Checkout.serializers import *
from rest_framework import authentication, permissions

from Checkout.permissions import *

class CarritoComprasAPI(viewsets.ViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = ()
    def list(self, request):
        carritos = CarritoCompras.objects.all()
        serializer = CarritoSerial(carritos, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CarritoSerial(data=request.data)
        if serializer.is_valid():
            carrito = serializer.save()
            return Response({'idCarrito':carrito.id})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        data = {'pagado':True}
        serializer = CarritoSerial(carrito, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class ArticulosAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializer = ArticuloSerial(articulos, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticuloSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Creados':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        #Permite actualizar atributos de nuestros objetos CRUD
        carrito = CarritoCompras.objects.get(pk=pk)
        carritoS = CarritoSerial(carrito, request.data, partial=True)
        if carritoS.is_valid():
            carritoS.save()
            return Response({"Actualizado":True})
        return Response(carritoS.errors, status=HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, pk=None):
        #Permite actualizar TODOS los argumentos en base de datos
        carrito = CarritoCompras.objects.get(pk=pk)
        carritoS = CarritoSerial(carrito, request.data)
        if carritoS.is_valid():
            carritoS.save()
            return Response({"Actualizado":True})
        return Response(carritoS.errors, status=HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        carrito = CarritoCompras.objects.get(pk=pk)
        carrito.delete()
        return Response({"Delete":True})

class InfoEnvioAPI(viewsets.ViewSet):
    def create(self, request):
        serializer = ArticuloSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Creados':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        info = get_object_or_404(InfoEnvio, pk=pk)
        serializer = CarritoSerial(info, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)