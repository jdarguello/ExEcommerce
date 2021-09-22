from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from .serializers import *


class CarritoComprasAPI(viewsets.ViewSet):
    def list (self, request):         #lista una serie de componentes de la base de datos
        # request peticiones de usuario (GET, POST)
        carritos = CarritoCompras.objects.all()
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create (self, request):

        #nuevoCarritos = CarritoCompras.objects.create(usuario = request.data["usuario"], dcto=request.data["dcto"], cantMinima=request.data["cantMinima"])

        serialCarrito = CarritoSerial(data=request.data)
        if serialCarrito.is_valid():
            serialCarrito.save()
            return Response({"Exito": True})
        return Response(serialCarrito.errors)

    def retrieve(selfself, request, pk=None):
#pk primary key es decir argumento que permite indentificar u obtener
#retrieve enviar la informacion de uno o varios objetos
        carritosUsuarios = CarritoCompras.objects.filter(usuario=pk)
        carritoS= CarritoSerial(carritosUsuarios, many= True)
        return Response(carritoS.data)

    def partial_update(self, request, pk=None):
        carrito = get_object_or_404(CarritoCompras, pk=pk)
        data = {'pagado': True}
        serializer = CarritoSerial(carrito, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update': True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class ArticulosAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializador = ArticuloSerial(articulos, many=True)
        return Response(serializador.data)

    def create(self, request):
        serializadorArticulo = ArticuloSerial(data=request.data)
        if serializadorArticulo.is_valid():
            serializadorArticulo.save()
            return Response({"Exito":True})
        return Response(serializadorArticulo.errors)

    def retrieve(self, request, pk= None):
        articulos= Articulo.objects.get(pk=pk)
        serializador= ArticuloSerial(articulos)
        return Response(serializador.data)


    def partial_update(self, request, pk=None):
        artModificar = Articulo.objects.get(pk=pk)
        serializador=ArticuloSerial(artModificar, request.data, partial= True)
        if serializador.is_valid():
            serializador.save()
            return Response({"Actualizado":True})
        return Response (serializador.errors)

    def destroy(self, request, pk=None):
        pass


