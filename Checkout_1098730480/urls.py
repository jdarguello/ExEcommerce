#Contiene las direcciones locales de la aplicación 'Checkout'

from django.urls import path, include

from rest_framework.routers import DefaultRouter

#ViewSet => especificamos las rutas mediante 'routers'

from Checkout_1098730480.views import *    #=> from Checkout_1098384.views import *

router = DefaultRouter()    #=> agregamos las direcciones de nuestroos ViewSets

router.register('carrito', CarritoAPI, basename="carrito")

urlpatterns = [
    #Lista de direcciones locales
    path('crud/', include(router.urls))
]