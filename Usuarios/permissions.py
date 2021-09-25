#Crearemos permisos de usario para nuestra aplicación

from rest_framework.permissions import BasePermission

class AccesoInfoPersonal(BasePermission):
    #Brindar permiso de acceso y manipulación de información
    #siempre que el usuario que desea acceder sea el dueño

    def has_object_permission(self, request, view, obj):
        #request => contiene TODA la información del usuario que desea acceder
        #view => Objeto de tipo API

        #obj => corresponde al objeto CRUD sobre el que desea manipular

        #Lógica: si el usuario (request.user) es dueño del perfil/cuenta (obj)
        #brinde acceso (True); de lo contrario: lo negamos (False); a menos,
        #que se trate de un usuario administrador
        
        
        if request.user.is_staff:
            return True #Brinda acceso a usuarios de tipo administrador
            
        #Ahora, si no es de tipo administrador...

        print(obj)

        #lógica si se busca manipular información del usuario 

        #hasattr() => identifica si hay un atributo en un objeto Python

        if hasattr(obj, 'username'):
            #Identifica que vamos a analizar un objeto 'User'
            if request.user.username == obj.username:
                return True
        else:
            #Análisis de objeto tipo 'Perfil'
            if request.user.username == obj.usuario.username:
                return True
        return False 

        




        


