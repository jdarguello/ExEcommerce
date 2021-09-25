from rest_framework import serializers

from django.contrib.auth import get_user_model

from Usuarios.models import *


#1. usuarios
class UserSerial(serializers.ModelSerializer):
    #Permite convertir los usuarios CRUD en diccionarios Python
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

        extra_kwargs = {    #Proteger contraseña de usuarios
            'password': {
                'write_only':True,  #=> sólo permite escritura de contraseña
                'style': {
                    'input_type':'password' #=> brinda el estilo de contra (***)
                }
            }
        }

        #kwargs => Keyword arguments -> diccionarios

#2. Perfiles
class PerfilSerial (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

