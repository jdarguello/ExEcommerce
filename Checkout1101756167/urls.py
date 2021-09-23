
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register ('carrito', CarritoComprasAPI, basename="carrito")
router.register ('articulos', ArticuloAPI, basename="articulos")
router.register ('envio', InfoEnvioAPI, basename="envio")

urlpatterns = [
    path('crud/', include(router.urls))
    
]