from django.db import models

from django.contrib.auth import get_user_model

class Perfil (models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        #Identificación del objeto
        return self.usuario.username
    
    @property
    def infoUsuario(self):
        #Ejecutamos desarrollo para obtener info de usuario
        pass