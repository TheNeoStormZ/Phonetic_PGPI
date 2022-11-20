from django.db import models
from enum import Enum
from django.core.validators import MinValueValidator


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
