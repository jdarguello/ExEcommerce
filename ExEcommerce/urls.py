from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include('Productos.urls')),

    path('checkout/api/', include('checkout1098681166_1.urls')),

    path('checkout/api/', include('Checkout_1098730480.urls'))

]
