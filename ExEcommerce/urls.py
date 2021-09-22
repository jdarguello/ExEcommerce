from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include('Productos.urls')),
    path("checkout/api/", include("checkout_80159226.urls"))
]
