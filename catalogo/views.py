from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import principal.models as models
from django.core import serializers
from django.http import JsonResponse
 
def catalogo(request):
  template = loader.get_template('catalogo.html')
  productos = models.Producto.objects.all().values()
  lista_categorias = [categoria for categoria in models.Producto.objects.values_list('categoria', flat=True).distinct()]
  context = {
    'productos':productos,
    'categorias':lista_categorias
  }
  return HttpResponse(template.render(context, request))

def search(request):
    if "q" in request.GET:
        query = request.GET["q"].strip()
        prods  = models.Producto.objects.filter(nombre__icontains=query).all()
        
        data = serializers.serialize("json", prods)
        
        return JsonResponse(prods, safe=False)

