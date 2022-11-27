from django.db import models
from enum import Enum
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User



class ProductType(Enum):   # A subclass of Enum
    FUND = "Funda"
    CARG = "Cargadores"
    PROT = "Protectores"
    OTRO = "Otros"

class ProductSections(Enum):   # A subclass of Enum
    HUWI = "Huawei"
    XIAO = "Xiaomi"
    SAMG = "Samsung"
    VIVO = "Vivo"
    UNK = "Desconocido"


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.URLField()
    precio = models.DecimalField(decimal_places=2,max_digits=8,validators=[MinValueValidator(0)])
    categoria = models.CharField(max_length=15,choices=[(tag.value,tag.value) for tag in ProductType],default=ProductType.OTRO)
    secciones = models.CharField(max_length=15,choices=[(tag.value,tag.value) for tag in ProductSections],default=ProductSections.UNK)
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def _str_(self):
        return self.nombre
 

class CestaItem(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])

    def sum(self,mult):
        self.cantidad = self.cantidad + mult 
        return 0
    def rm(self,mult):
        self.cantidad = self.cantidad - mult
        return 0

class Cesta(models.Model):

    usuario = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(CestaItem)

    def _str_(self):
        return self.items.all()

    def get_total_price(self):
        if self.items is None:
            return 0
        else:
            cestaItems = [item for item in self.items.all()]
            return sum([item.producto.precio*item.cantidad for item in cestaItems])

    def get_productos(self):
        if self.items is None:
            return []
        else:
            cestaItems = [item for item in self.items.all()]
            return cestaItems

    def delete_cesta_item(self,cestaItem):
        self.items.remove(cestaItem)
        return 0
    def add_cestaitem(self,cestaitem):
        self.items.add(cestaitem)
        return 0


