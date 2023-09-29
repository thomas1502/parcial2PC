from django.contrib import admin
from .models import Producto, Venta, Detalle, Solicitud

# Register your models here.

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle)
admin.site.register(Solicitud)