from django.urls.resolvers import URLPattern
from checkout1026301065.views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("carrito",CarritoCompraAPI,basename="carrito")
router.register("articulo",ArticuloAPI,basename="articulo")
router.register("infoenvio",InfoEnvioAPI,basename="envio")
urlpatterns=[path("crud/",include(router.urls))
]

