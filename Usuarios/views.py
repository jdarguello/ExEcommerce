from rest_framework import viewsets
from rest_framework import authentication, permissions

from django.contrib.auth import get_user_model

from Usuarios.serializers import *
from Usuarios.permissions import AccesoInfoPersonal


class UsuariosAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,AccesoInfoPersonal)
    serializer_class = UserSerial
    queryset = get_user_model().objects.all()
    #queryset => especifica los objetos CRUD que se desean enviar a través del API 



class PerfilesAPI (viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AccesoInfoPersonal)
    serializer_class = PerfilSerial
    queryset = Perfil.objects.all()