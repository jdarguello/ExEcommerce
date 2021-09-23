from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from .serializers import CarritoSerial, InfoEnvioSerial, ArticuloSerial
from .models import CarritoCompra, InfoEnvio, Articulo


class CarritoAPI(viewsets.ViewSet):
    def list(self, request):
        # listar infromación
        # request => peticion de user. GET, POST, PUT, ...
        carritos = CarritoCompra.objects.all() # obj tipo CarritoCompra
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create(self, request) :
        # crear obj en DB
        # nuevoCarrito = CarritoCompra.objects.create(usuario=request.data)
        serializador = CarritoCompra(data=request.data)
        if serializador.is_valid():
            carrito = serializador.save()
            return Response({'idCarrito':carrito.id})
        return Response(serializador.errors, HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk=None):
        # obtetner un solo reg en DB
        #pk = primary key
        carrito = get_object_or_404(CarritoCompra, id=pk)
        seriarizador = CarritoSerial(carrito)
        return Response(seriarizador.data)

    
    def partial_update(self, request, pk=None):
        # actualizar parcial => PATCH
        carrito = get_object_or_404(CarritoCompra, pk=pk)
        carrito_s = CarritoSerial(carrito, request.data, partial=True)
        if carrito_s.is_valid():
            carrito_s.save()
            return Response({'Actualizado':True})
        return Response(carrito_s.errors, HTTP_400_BAD_REQUEST)


    # No recomendado para carrito de compra -- No queremos cambiar user
    def update(self, request, pk=None):
        # actualizar parcial => PUT
        carrito = get_object_or_404(CarritoCompra, pk=pk)
        carrito_s = CarritoSerial(carrito, request.data, partial=False)
        if carrito_s.is_valid():
            carrito_s.save()
            return Response({'Actualizado':True})
        return Response(carrito_s.errors)


    def destroy(self, request, pk=None):
        # borramos elementos en DB
        carrito = CarritoCompra.objects.get(pk)
        carrito.delete()
        return Response({'Objeto borrado':True})

    
#    def retrive(self, request, pk=None):
#       return Response(pk)


class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        articulo = Articulo.objects.all()
        serializer = ArticuloSerial(articulo, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = Articulo(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Arituculo creado':True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class InfoEnvioAPI(viewsets.ViewSet):
    def list(self, request):
        info_envio = InfoEnvio.objects.all()
        serializer = InfoEnvioSerial(info_envio, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = InfoEnvio(data=request.data)
        if serializer.is_valid():
            info_e = serializer.save()
            return Response({'Envio Creado': True, 'infoId':info_e.id})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        info_envio = get_object_or_404(InfoEnvio, id=pk)
        seriarizer = InfoEnvioSerial(info_envio)
        return Response(seriarizer.data)


    def partial_update(self, request, pk=None):
        # actualizar parcial => PATCH
        info_envio = get_object_or_404(InfoEnvio, pk=pk)
        info_envio_s = InfoEnvioSerial(info_envio, request.data, partial=True)
        if info_envio_s.is_valid():
            info_envio_s.save()
            return Response({'Info Envio Actualizado':True})
        return Response(info_envio_s.errors)


    def destroy(self, request, pk=None):
        # borramos elementos en DB
        info_envio = InfoEnvio.objects.get(pk)
        info_envio.delete()
        return Response({'Info envio Borrado':True})

    

'''
class CarritoAPI(viewsets.ModelViewSet):
    serializer_class = CarritoSerial
    queryset = CarritoCompra.objects.all()
'''