from django.contrib import admin

from .models import Producto, Cesta, CestaItem, Pedido

admin.site.register(Producto)
admin.site.register(Cesta)
admin.site.register(CestaItem)
admin.site.register(Pedido)

# Register your models here.
