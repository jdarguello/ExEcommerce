# Direcciones de las APIS
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('carrito', CarritoAPI, basename="Carrito")
router.register('articulo', ArticuloAPI, basename="Articulo")
router.register('info_envio', InfoEnvioAPI, basename="Info Envio")

urlpatterns = [
    path('crud/', include(router.urls))
]
