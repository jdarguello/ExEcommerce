#Especificamos las direcciones de las API's

from checkout1098681166_1.views import CarritoComprasAPI
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Productos.views import ProductoAPI, TipoAPI, ComentarioAPI

from .views import *

router = DefaultRouter()
router.register('tipo', TipoAPI)
router.register('producto', ProductoAPI)
router.register('comentario', ComentarioAPI, basename="comentario")
router.register('carrito', CarritoComprasAPI, basename="carrito")

urlpatterns = [
    path('crud/', include(router.urls))
   
]

#localhost:8000/productos/api/crud/tipo
