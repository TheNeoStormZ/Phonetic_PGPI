from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import principal.models as models
 
def index (request):
  productos = models.Producto.objects.all().values()[:6]
  template = loader.get_template('inicio.html')
  context = {
    'productos': productos
  }
  return HttpResponse(template.render(context, request))
  
def catalogo(request):
  template = loader.get_template('catalogo.html')
  productos = models.Producto.objects.all().values()
  lista_categorias = [categoria for categoria in models.Producto.objects.values_list('categoria', flat=True).distinct()]
  context = {
    'productos':productos,
    'categorias':lista_categorias
  }
  return HttpResponse(template.render(context, request))          


def producto(request):
  template = loader.get_template('producto.html')
  context = {
  }
  return HttpResponse(template.render(context, request))