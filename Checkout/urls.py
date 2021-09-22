from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import *
# Viewset => especificamos las rutas mediante 'routers'

router = DefaultRouter() #> agregamos las direccines de nuestros viewsets

router.register('carrito', CarritoAPI, basename="carrito")
router.register('articulo', ArticuloAPI, basename="articulo")
router.register('infoEnvio', InfoEnvioAPI, basename="infoEnvio")

urlpatterns = [
    #Lista de direcciones locales
    path('crud/', include(router.urls))
]
