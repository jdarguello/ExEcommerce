#Gestionamos las direcciones locales de la aplicación 'Usuarios'

from django.urls import path, include #=> crear una nueva dirección (path). include => gestiona múltiples direcciones

from rest_framework.routers import DefaultRouter   

#DefaultRouter => se emplea para el registro de direcciones de API's tipo ViewSet

from Usuarios.views import *    #=> importa todas las API's

router = DefaultRouter()
router.register('usuarios', UsuariosAPI)
router.register('perfiles', PerfilesAPI)

urlpatterns = [
    #Sección en donde se realiza la gestión de direcciones url locales
    path('crud/', include(router.urls))
]