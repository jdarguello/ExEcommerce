from django.urls import path,include
from rest_framework import urlpatterns

from rest_framework.routers import DefaultRouter
from checkout1073246233.views import *

router = DefaultRouter()

router.register('carrito',CarritoComprasAPI,basename='Carrito')
router.register('articulos',ArticulosAPI,basename='Articulo')
router.register('infoenvio',InfoAPI,basename='Info')

urlpatterns = [
    path('crud/',include(router.urls))
]