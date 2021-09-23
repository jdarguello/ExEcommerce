from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include('Productos.urls')),
    path('checkout/api/', include('checkout80035296.urls')),
    path('checkout/api/', include('Checkout_1098730480.urls'))
]
