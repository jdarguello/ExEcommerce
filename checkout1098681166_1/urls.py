from checkout1098681166_1.views import CarritoComprasAPI
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename="carrito")
router.register('articulo', ArticuloAPI, basename="articulo")

urlpatterns = [
    path('crud/', include(router.urls))

]

#localhost:8000/productos/api/crud/tipo