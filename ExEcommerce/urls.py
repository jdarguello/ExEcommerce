from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include('Productos.urls')),
    path('checkout/api/', include('Checkout_1095834454.urls'))
]
