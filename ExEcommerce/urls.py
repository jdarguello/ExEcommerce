from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include('Productos.urls')),

    path('checkout31/api/', include('checkout31.urls')),

    path('checkout/api/', include('Checkout.urls'))

]
