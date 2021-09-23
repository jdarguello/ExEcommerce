from checkout1098681166_1.models import Articulo, CarritoCompras, InfoEnvio
from django.contrib import admin

from checkout1098681166_1.models import *

# Register your models here.

admin.site.register(CarritoCompras)
admin.site.register(Articulo)
admin.site.register(InfoEnvio)
