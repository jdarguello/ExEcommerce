from django.urls import path, include

from rest_framework.routers import DefaultRouter

#viesets trabajan las direcciones internas con Routers

from .views import *
router = DefaultRouter()
router.register("carrito", CarritoComprasAPI, basename="carrito")
router.register("articulos", ArticulosAPI,basename="articulos")
urlpatterns =[
    path("crud/", include(router.urls))
]
