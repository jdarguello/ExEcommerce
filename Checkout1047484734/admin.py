from Checkout1047484734.models import Articulo, CarritoCompras, InfoEnvio
from django.contrib import admin
from .models import *

admin.site.register(CarritoCompras)
admin.site.register(Articulo)
admin.site.register(InfoEnvio)
