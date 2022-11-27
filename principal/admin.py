from django.contrib import admin

from .models import Producto, Cesta, CestaItem

admin.site.register(Producto)
admin.site.register(Cesta)
admin.site.register(CestaItem)

# Register your models here.
