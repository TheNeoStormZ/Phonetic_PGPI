from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Producto
 
def index (request):
  productos = Producto.objects.all().values()[:6]
  template = loader.get_template('inicio.html')
  context = {
    'productos': productos
  }
  return HttpResponse(template.render(context, request))