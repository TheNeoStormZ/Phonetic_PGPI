from principal.models import Producto
from django.http import HttpResponse
from django.template import loader
#import principal.models as models
 
def index (request):
  productos = Producto.objects.all().values()[:6]
  template = loader.get_template('inicio.html')
  context = {
    'productos': productos
  }
  return HttpResponse(template.render(context, request))
  
def catalogo(request):
  template = loader.get_template('catalogo.html')
  productos = Producto.objects.all().values()
  lista_categorias = [categoria for categoria in Producto.objects.values_list('categoria', flat=True).distinct()]
  context = {
    'productos':productos,
    'categorias':lista_categorias
  }
  return HttpResponse(template.render(context, request))       
  
def secciones(request):
  template = loader.get_template('secciones.html')
  productos = Producto.objects.all().values()
  lista_secciones = [secciones for secciones in Producto.objects.values_list('secciones', flat=True).distinct()]
  context = {
    'productos':productos,
    'secciones':lista_secciones
  }
  return HttpResponse(template.render(context, request))      

def producto(request, producto_id=''):
  template = loader.get_template('producto.html')
  producto = Producto.objects.filter(id=producto_id).values()
  context = {
    'producto':producto[0]
  }
  return HttpResponse(template.render(context, request))

def busqueda(request):
  template = loader.get_template('inicio.html')
  q = request.GET.get('q', '')
  if q:
      qset = (
        Producto(nombre__icontains=q)
        )
      results = Producto.objects.filter(qset).distinct()
  else:
        results = []
  context = {
    'productos':results
  }
  return HttpResponse(template.render(context, request))

def search(request):
  query = request.GET.get('q', '')
  if query:
      qset = (
          Q(title__icontains=query) |
          Q(authors__first_name__icontains=query) |
          Q(authors__last_name__icontains=query)
      )
      results = Book.objects.filter(qset).distinct()
  else:
      results = []
  return render_to_response("books/search.html", {
      "results": results,
      "query": query
  })