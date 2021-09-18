#Especificamos las direcciones de las API's

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Productos.views import ProductoAPI, TipoAPI, ComentarioAPI

router = DefaultRouter()
router.register('tipo', TipoAPI)
router.register('producto', ProductoAPI)
router.register('comentario', ComentarioAPI, basename="comentario")

urlpatterns = [
    path('crud/', include(router.urls))
]

#localhost:8000/productos/api/crud/tipo