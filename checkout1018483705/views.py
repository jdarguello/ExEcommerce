#from django.shortcuts import render # Esto no se usa
from rest_framework import viewsets
from rest_framework.response import Response # Crear una respuesta para un método que se active de los serializadores
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import *# from checkout1018483705.serializers import *



# Create your views here.

class CarritoComprasAPI(viewsets.ViewSet):
    def list(self, request):
        # request => se trata de la petición de usuario: get, post, put...
        carritos = CarritoCompras.objects.all()
        carritosSerial = CarritoSerial(carritos, many=True) # el many = True es para que traiga varios objetos
        return Response(carritosSerial.data)
    
    def create(self, request):
        # Crear nuevos elementos en base de datos
        #nuevoCarrito = CarritoCompras.objects.create(usuario=request.data["usuario"], )
        nuveoCarritoSerial = CarritoSerial(data= request.data)
        if nuveoCarritoSerial.is_valid():
            nuveoCarritoSerial.save()
            return Response({"Exito":True})
        #return Response(request.data)
        return Response(nuveoCarritoSerial.errors, status=HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        # Obtener uno a varios objetos de la base de datos, generalmente para un solo objeto
        # ok -> llave primario - método de identifiación de nuestros objetos
        carritos = CarritoCompras.objects.get(pk=pk)
        serializador = CarritoSerial(carritos) # antes era many=True, pero como solo es uno 

        return Response(serializador.data)

    def partial_update(self, request, pk=None):
        # Permite actuzalizar los atributos de nuestro CRUD
        carrito = CarritoCompras.objects.get(pk=pk)
        carrSer = CarritoSerial(carrito, request.data, partial= True)
        if carrSer.is_valid():
            carrSer.save()
            return Response({"Actualizado":True})
        return Response(carrSer.errors)
    
    def update (self, request, pk=None):
        # Permite la actualización completa del registro en base de datos
        carrito = CarritoCompras.objects.get(pk=pk)
        carrSer = CarritoSerial(carrito, request.data, partial= True)
        if carrSer.is_valid():
            carrSer.save()
            return Response({"Actualizado":True})
        return Response(carrSer.errors)

    def destroy (self, request, pk= None):
        carrito = CarritoCompras.objects.get(pk=pk)
        carrito.delete()
        return Response({"Delete":True})
        


class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        artiserial = ArticuloSerial(articulos,many=True)   
        return Response(artiserial.data)

    def create(self, request):
        newArtSerial = ArticuloSerial(data= request.data)
        if newArtSerial.is_valid():
            newArtSerial.save()
            return Response({"Exito":True})
        #return Response(request.data["Hola"]) # Si entra {"Hola":"Mundo"} retorna "Mundo"
        return Response(newArtSerial.errors)
    
    def retrieve(self, request, pk=None):
        articulo = Articulo.objects.get(pk=pk)
        artSerial = ArticuloSerial(articulo)
        return Response(artSerial.data)
    
    

class InfoEnvioAPI (viewsets.ViewSet):
    def list(self, request):
        infoEnvios = InfoEnvio.objects.all()
        infoserial = InfoSerial(infoEnvios, many=True)

        return Response(infoserial.data)

    def create(self, request):

        newInfoSerial = InfoSerial(data=request.data)
        if newInfoSerial.is_valid():
            newInfoSerial.save()
            Response({"Exito":True})
        return Response(newInfoSerial.errors)
        #return Response(request.data["Hola"])

    def retrieve(self, request, pk=None):
        infoEnvio = InfoEnvio.objects.get(pk=pk)
        infserial = InfoSerial(infoEnvio)
        return Response(infserial.data)