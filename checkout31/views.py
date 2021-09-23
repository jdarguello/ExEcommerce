from rest_framework import viewsets
from rest_framework.response import Response
from checkout31.serializers import *

class carrito_compras_api ( viewsets.ViewSet):
    def list(self,request):
        carritos = carrito_compras.objects.all()
        serializador = carrito_compras_serial(carritos, many = True)
        return Response(serializador.data)

    def create (self, request): 
        nuevocarritoserial = carrito_compras_serial(data = request.data)
        if nuevocarritoserial.is_valid():
            nuevocarritoserial.save()
            return Response({"exit" : "objeto guardado" })
        return Response(nuevocarritoserial.errors)

    def retrieve(self, request, pk = None):
        #carrito = carrito_compras.objects.filter(usuario = pk)
        #serializador = carrito_compras_serial(carrito, many = True)
        carrito = carrito_compras.objects.get(pk = pk)
        serializador = carrito_compras_serial(carrito)
        return Response(serializador.data)

    def partial_update(self, request, pk= None):
        carrito = carrito_compras.objects.get(pk=pk)
        carritoserial = carrito_compras_serial(carrito,request.data, partial = True)
        if carritoserial.is_valid():
            carritoserial.save()
            return Response({"exit" : "actualizado" })
        return Response(carritoserial.errors)

    def update (self,request,pk=None):
        carrito = carrito_compras.objects.get(pk=pk)
        carritoserial = carrito_compras_serial(carrito,request.data)
        if carritoserial.is_valid():
            carritoserial.save()
            return Response({"exit" : "actualizado total" })
        return Response(carritoserial.errors)

    def destroy (self, request, pk=None):
        carrito = carrito_compras.objects.get(pk=pk)
        carrito.delete()
        return Response({"Delete" : "eliminado"})

class articulo_api (viewsets.ViewSet):
    def list(self,request):
        articulos = articulo.objects.all()
        serializador = articulo_serial(articulos, many = True)
        return Response(serializador.data)

    def create (self, request): 
        articuloserial = articulo_serial(data = request.data)
        if articuloserial.is_valid():
            articuloserial.save()
            return Response({"exit" : "objeto guardado" })
        return Response(articuloserial.errors)

    def retrieve(self, request, pk = None):
        Articulo = articulo.objects.get(pk = pk)
        serializador = articulo_serial(Articulo)
        return Response(serializador.data)

    def partial_update(self, request, pk= None):
        Articulo = articulo.objects.get(pk=pk)
        articuloserial = articulo_serial(Articulo,request.data, partial = True)
        if articuloserial.is_valid():
            articuloserial.save()
            return Response({"exit" : "actualizado" })
        return Response(articuloserial.errors)

    def destroy (self, request, pk=None):
        Articulo = articulo.objects.get(pk=pk)
        Articulo.delete()
        return Response({"Delete" : "eliminado"})

class info_envio_api(viewsets.ViewSet):
    def list(self, request):
        info_envios = info_envio.objects.all()
        serializador = info_envio_serial(info_envios, many = True )
        return Response(serializador.data)

    def create (self, request): 
        infoserial = info_envio_serial(data = request.data)
        if infoserial.is_valid():
            infoserial.save()
            return Response({"exit" : "informacion guardada" })
        return Response(infoserial.errors)

    def retrieve(self, request, pk = None):
        info = info_envio.objects.get(pk = pk)
        serializador = info_envio_serial(info)
        return Response(serializador.data)

    def partial_update(self, request, pk= None):
        info = info_envio.objects.get(pk=pk)
        infoserial = info_envio_serial(info,request.data, partial = True)
        if infoserial.is_valid():
            infoserial.save()
            return Response({"exit" : "informacion actualizada" })
        return Response(infoserial.errors)

    def destroy (self, request, pk=None):
        info = info_envio.objects.get(pk=pk)
        info.delete()
        return Response({"Delete" : "eliminado"})