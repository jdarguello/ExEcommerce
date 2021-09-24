#gestionar las direcciones internas de la aplicacion chechout
from django.urls import path, include
from rest_framework import routers, urlpatterns
#ViewSets necesita trabajar con routers
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename='carrito')

urlpatterns = [
    path('crud/', include(router.urls))
]

