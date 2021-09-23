
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from cheackout1130619212.views import *

router = DefaultRouter()
router.register('Carrito', CarritoAPI)
router.register('Articulo',ArticuloAPI,basename='Arti')
router.register('Info',InfoAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]

#localhost:8000/cheackout/api/crud/