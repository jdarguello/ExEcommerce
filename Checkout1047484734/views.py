from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework.status import HTTP_400_BAD_REQUEST

class CarritoComprasAPI (viewsets.ViewSet):
    def list(self, request):
        #request trata de la peticion de usuario get,post, put...
        carritos = CarritoCompras.objects.all()
        carritoSerializador = CarritoComprasSerial(carritos, many=True)
        return Response(carritoSerializador.data)

    def create(self, request):
        #crear nuevos elementos en base de datos
        #request.data = [{},{},...]
        #nuevoCarritoSerial = CarritoComprasSerial(data=request.data, many=True)
        nuevoCarritoSerial = CarritoComprasSerial(data=request.data)
        if nuevoCarritoSerial.is_valid():
            nuevoCarritoSerial.save()
            return Response({"Exite":True})
        return Response(nuevoCarritoSerial.errors, status=HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        #obtener una información de la base de datos de un objeto
        carritos = CarritoCompras.objects.filter(usuario=pk)
        serializador = CarritoComprasSerial(carritos, many=True)
        return Response(serializador.data)

    def parcial_update(self, request, pk=None):
        #permite actualizar atributos de nuestro objeto CRUD
        carrito = CarritoCompras.objects.get(pk=pk)
        carritos = CarritoComprasSerial(carrito, request.data, partial=True)
        if carritos.is_valid():
            carritos.save()
            return Response({"Actualizado":True})
        return Response(carritos.errors,status=HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        #permite actuazliar todos los argumentos en base de datos
        carrito = CarritoCompras.objects.get(pk=pk)
        carritos = CarritoComprasSerial(carrito, request.data)
        if carritos.is_valid():
            carritos.save()
            return Response({"Actualizado":True})
        return Response(carritos.errors,status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        carrito = CarritoCompras.objects.get(pk=pk)
        carrito.delete()
        return Response({"Delete":True})