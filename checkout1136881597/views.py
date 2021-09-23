from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import *

class carritoComprasAPI (viewsets.ViewSet):
    def list(self, request):
        #request => peticiones de usuario (GET, POST)
        #list => cumple el objetivo de listar una serie de componentes de la base de datos
        carritos = carritoCompras.objects.all()
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create(self, request):
        #Crear registros en base de datos
        #nuevoCarrito = CarritoCompras.objects.create(usuario = request.data["usuario"], dcto=request.data["dcto"], cantMinima = request.data["cantMinima"])
        serialCarrito = CarritoSerial(data=request.data)
        if serialCarrito.is_valid():
            serialCarrito.save()
            return Response({"Exito": True})
        return Response(serialCarrito.errors)

    def retrieve(self, request, pk=None):
        #pk => primary key -> es decir: argumento que permite identificar y obtener objetos
        #retrieve => enviar la información de uno o varios objetos
        carritosUsuario = carritoCompras.objects.filter(usuario=pk)
        carritoS = CarritoSerial(carritosUsuario, many=True)
        return Response(carritoS.data)

class ArticuloAPPI (viewsets.ViewSet):
    def list(self, request):
        #request => peticiones de usuario
        #list => cumple el objetivo de listar una serie de registros
        articulos = articulo.objects.all()
        serializador = ArticuloSerial(articulos, many=True)
        return Response(serializador.data)
    
    def create(self, request):
        serializadorArticulo = ArticuloSerial(data=request.data)
        if serializadorArticulo.is_valid():
            serializadorArticulo.save()
            return Response({'Exito':True})
        return Response(serializadorArticulo.errors)

    def retrieve(self, request, pk=None):
        articulos = articulo.objects.get(pk=pk)
        serializador = ArticuloSerial(articulos)
        return Response(serializador.data)

        

    def partial_update(self, request, pk=None):
        artModificar = articulo.objects.get(pk=pk)
        serializador = ArticuloSerial(artModificar, request.data, partial=True)
        if serializador.is_valid():
            serializador.save()
            return Response({'Actualizado':True})
        return Response(serializador.errors)

    def destroy(self, request, pk=None):
        pass



    

