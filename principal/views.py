from principal.models import Producto
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
#import principal.models as models
 
def index (request):
  productos = Producto.objects.all().values()[:6]
  template = loader.get_template('inicio.html')
  context = {
    'productos': productos,
    'busqueda': '',
  }
  return HttpResponse(template.render(context, request))
  
def catalogo(request):
  template = loader.get_template('catalogo.html')
  productos = Producto.objects.all().values()
  lista_categorias = [categoria for categoria in Producto.objects.values_list('categoria', flat=True).distinct()]
  context = {
    'productos':productos,
    'categorias':lista_categorias,
  }
  return HttpResponse(template.render(context, request))       
  
def secciones(request, seccion_nombre='Desconocido'):
  template = loader.get_template('secciones.html')
  productos = Producto.objects.filter(secciones=seccion_nombre).values()
  lista_secciones = [secciones for secciones in Producto.objects.values_list('secciones', flat=True).distinct()]
  context = {
    'productos':productos,
    'seccion':seccion_nombre,
  }
  return HttpResponse(template.render(context, request))      

def producto(request, producto_id=''):
  template = loader.get_template('producto.html')
  producto = Producto.objects.filter(id=producto_id).values()
  context = {
    'producto':producto[0]
  }
  return HttpResponse(template.render(context, request))

def buscar(request):
  template = loader.get_template('inicio.html')
  buscar = request.GET.get('q', None)
  productos = Producto.objects.filter(Q(nombre__icontains=buscar) | Q(categoria__icontains=buscar) | Q(secciones__icontains=buscar))
  context = {
    'productos':productos,
    'busqueda':buscar,
  }
  return HttpResponse(template.render(context, request))

def terminos(request):
  template = loader.get_template('terminos.html')
  context = {}
  return HttpResponse(template.render(context, request))

def privacidad(request):
  template = loader.get_template('privacidad.html')
  context = {}
  return HttpResponse(template.render(context, request))

def conocenos(request):
  template = loader.get_template('conocenos.html')
  context = {}
  return HttpResponse(template.render(context, request))
