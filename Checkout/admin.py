from Checkout.models import Articulo, CarritoCompras, InfoEnvio
from django.contrib import admin

# Register your models here.
admin.site.register(CarritoCompras)
admin.site.register(Articulo)
admin.site.register(InfoEnvio)