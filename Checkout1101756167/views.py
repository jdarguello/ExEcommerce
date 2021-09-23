from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import *


class CarritoComprasAPI(viewsets.ViewSet):
    def list(self, request):
        carritos = CarritoCompras.objects.all()
        serializer = CarritoComprasSerial(carritos, many=True)
        return Response(serializer.data)
   
    def create(self, request):
        serializer = CarritoComprasSerial(data=request.data)
        if serializer.is_valid():
            carrito = serializer.save()
            return Response({'idCarrito':carrito.id})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        #pk= primaryKey
        carritosUsuario = CarritoCompras.objects.filter(usuario=pk)
        carritoS= CarritoComprasSerial(carritosUsuario,many=True)
        return Response(carritoS.data)
    
    def partial_update(self, request, pk=None):
        carrito = self.get_object()
        data = {'pagado':True}
        serializer = CarritoComprasSerial(carrito, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializer = ArticuloSerial(articulos, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticuloSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Exito':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        #pk= primaryKey
        articulos = Articulo.objects.get(pk=pk)
        artS= ArticuloSerial(articulos,many=True)
        return Response(artS.data)

    def partial_update(self, request, pk=None):
        artModificar = Articulo.objects.get(pk=pk)
        serializer = ArticuloSerial(artModificar, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Actualizado":True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def destroy (self, request, pk= None):
        pass    

class InfoEnvioAPI(viewsets.ViewSet):
    def list(self, request):
        envios = InfoEnvio.objects.all()
        serializer = InfoEnvioSerial(envios, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = InfoEnvioSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Creados':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        #pk= primaryKey
        enviosUsuario = InfoEnvio.objects.filter(carrito=pk)
        envioS= InfoEnvioSerial(enviosUsuario,many=True)
        return Response(envioS.data)