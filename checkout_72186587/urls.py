#Especificamos las direcciones de las API's

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from checkout_72186587.views import * 

#CarritoComprasAPI, ArticuloAPI, infoEnvioAPI

router = DefaultRouter()
router.register('Carrito', CarritoApi, basename="carrito")
router.register('Articulo', ArticuloApi, basename="articulo")
router.register('infoEnvio', InfoEnvioApi, basename="infoEnvio")

urlpatterns = [
    path('crud/', include(router.urls))
]

#localhost:8000/.../api/crud/tipos