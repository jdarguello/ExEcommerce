from checkout1136881597.views import ArticuloAPPI, carritoComprasAPI
from django.urls import path, include


from rest_framework.routers import DefaultRouter

#viewsets => trabajan las direciones internas con router

router = DefaultRouter()
router.register('carrito', carritoComprasAPI, basename="carrito")
router.register('articulos', ArticuloAPPI, basename='articulos')

urlpatterns = [
    path('crud/', include(router.urls))
]