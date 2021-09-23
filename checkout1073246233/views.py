from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from checkout1073246233.serializers import *
from checkout1073246233.models import *

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
    def retrieve(self, request, pk=None):
        #Obtener uno o varios objetos de la base de datos
        #pk -> llave primaria - metodo de identificacion de objetos
        carritos = CarritoCompras.objects.get(pk=pk)
        serializador = CarritoComprasSerial(carritos)
        return Response(serializador.data)
    
    def partial_update(self, request, pk=None):
        carrito = self.get_object()
        data = {'pagado':True}
        serializer = CarritoComprasSerial(carrito, data, partial=True)
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
    
    def retrieve(self,requets,pk=None):
        articulos = Articulo.objects.get(pk=pk)
        serializador = ArticuloSerial(articulos)
        return Response(serializador.data)

class InfoAPI(viewsets.ViewSet):
    def list(self,request):
        info = InfoEnvio.objects.all()
        serializador = InfoSerial(info,many=True)
        return Response(serializador.data)
    
    def create(self,request):
        serializador = InfoSerial(data = request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({'DatosListos':True})
        return Response(serializador.errors)
    
    def partial_update():
        pass