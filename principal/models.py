from django.db import models

# Create your models here.
class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.URLField()
    precio = models.IntegerField()
    stock = models.IntegerField()


    def _str_(self):
        return self.nombre
