from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import *



class CarritoAPI(viewsets.ViewSet):
    def list(self, request):
        #Listar información
        #request => petición de usuarios. GET, POST, PUT, ... 
        carritos = CarritoCompras.objects.all() #Son objetos del tipo 'CarritoCompras'
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create(self, request):
        #Crear registros en base de datos
        serializador = CarritoSerial(data=request.data)
        if serializador.is_valid():
            serializador.save() #Guarda el nuevo objeto
            return Response({"Exito":True}) #Creó el objeto
        return Response(serializador.errors)

 
    def retrieve(self, request, pk=None):
        #Obtener UN sólo registro en base de datos
        #pk => primary key
        carrito = get_object_or_404(CarritoCompras, pk=pk)
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



class CarritoAPI(viewsets.ModelViewSet):
    serializer_class = CarritoSerial
    queryset = CarritoCompras.objects.all()

    """
    def retrieve(self, request, pk=None):
        return Response(pk)
    """

"""
    def update():
        #Actualiza registros
        pass

    def partial_update():
        #Actualización parcial 
        pass

    def destroy():
        #borramos elementos en base de datos
        pass
"""