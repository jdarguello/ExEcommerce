from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import urlpatterns

from checkout31.views import *

router = DefaultRouter()

router.register('carrito',carrito_compras_api,basename = 'carrito')
router.register('articulo',articulo_api,basename='articulo')
router.register('info_envios',info_envio_api,basename='info_envios')

urlpatterns = [
    path('crud/',include(router.urls))
]

