#Gestión de permisos de 'Checkout'

from rest_framework.permissions import BasePermission

class PermisosCheckout(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            #Si el usuario, autenticado o no, desea crear carrito de compras
            return True #Permite a un usuario anónimo hacer compras
        
        #Si el usuario está registrado, permitir... PUT, PATCH y DELETE
        if request.user.is_authenticated and request.user.username == obj.usuario.usuario.username:
            return True
        
