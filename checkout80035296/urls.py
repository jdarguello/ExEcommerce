from django.db import router
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename="carrito")
router.register('infoenvio', InfoEnvioAPI, basename="infoenvio")
router.register('articulo', ArticuloAPI, basename="articulo")

urlpatterns = [
    path('crud/', include(router.urls)),
     
]