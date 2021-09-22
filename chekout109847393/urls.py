from django.urls import path, include

from rest_framework.routers import DefaultRouter

#ViewSets => trabajan las direcciones internas con routers 

from .views import *

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename="carrito")
router.register('articulos', ArticuloAPI, basename="articulos")

urlpatterns = [
    path('crud/', include(router.urls))
]
