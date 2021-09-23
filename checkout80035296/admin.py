from checkout80035296.models import Articulo, CarritoCompras, InfoEnvio
#from .models import * equivalente a la linea anterior
from django.contrib import admin

# Register your models here.
admin.site.register(CarritoCompras)
admin.site.register(InfoEnvio)
admin.site.register(Articulo)