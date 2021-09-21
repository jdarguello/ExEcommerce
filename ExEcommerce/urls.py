from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include('Productos.urls')),
    path('checkout/api/', include('cheackout1130619212.urls')),    
]
