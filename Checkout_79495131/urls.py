# Contiene las dir locales de la app Checkout
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ViewSet => especifi las rutas med 'routes'

from .views import CarritoAPI, InfoEnvioAPI

router = DefaultRouter()

router.register('carrito', CarritoAPI, basename='carrito')
router.register('infoenvio', InfoEnvioAPI, basename='infoenvio')

urlpatterns = [
    # lsita de dir locales
    path('crud/', include(router.urls))
]