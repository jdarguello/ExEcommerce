# Gestinamos las direcciones internas de la apicación checkout
from django.urls import path, include


#ViewSets => necesita trabajar con routers 
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename='Carrito')
router.register('articulo', ArticuloAPI, basename="Articulo")
router.register('infoenvio', InfoEnvioAPI, basename='InfoEnvio')

urlpatterns = [
    path('crud/', include(router.urls))
]