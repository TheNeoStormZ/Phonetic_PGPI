from principal.models import Producto, Cesta, CestaItem
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
#import principal.models as models
 
def index (request):
  productos = Producto.objects.all().values()[:6]
  cesta = Cesta.objects.filter(id=2)
  template = loader.get_template('inicio.html')
  context = {
    'productos': productos,
    'cesta': cesta[0].get_productos(),
    'precio_total': cesta[0].get_total_price(),
    'busqueda': '',
  }
  return HttpResponse(template.render(context, request))
  
def catalogo(request):
  template = loader.get_template('catalogo.html')
  productos = Producto.objects.all().values()
  cesta = Cesta.objects.filter(id=2)
  lista_categorias = [categoria for categoria in Producto.objects.values_list('categoria', flat=True).distinct()]
  context = {
    'productos':productos,
    'categorias':lista_categorias,
    'cesta': cesta[0].get_productos(),
    'precio_total': cesta[0].get_total_price(),
  }
  return HttpResponse(template.render(context, request))       
  
def secciones(request, seccion_nombre='Desconocido'):
  template = loader.get_template('secciones.html')
  productos = Producto.objects.filter(secciones=seccion_nombre).values()
  cesta = Cesta.objects.filter(id=2)
  lista_secciones = [secciones for secciones in Producto.objects.values_list('secciones', flat=True).distinct()]
  context = {
    'productos':productos,
    'seccion':seccion_nombre,
    'cesta': cesta[0].get_productos(),
    'precio_total': cesta[0].get_total_price(),
  }
  return HttpResponse(template.render(context, request))      

def producto(request, producto_id=''):
  template = loader.get_template('producto.html')
  producto = Producto.objects.filter(id=producto_id).values()
  cesta = Cesta.objects.filter(id=2)
  context = {
    'producto':producto[0],
     'cesta': cesta[0].get_productos(),
    'precio_total': cesta[0].get_total_price(),
  }
  return HttpResponse(template.render(context, request))

def buscar(request):
  template = loader.get_template('inicio.html')
  buscar = request.GET.get('q', None)
  productos = Producto.objects.filter(Q(nombre__icontains=buscar) | Q(categoria__icontains=buscar) | Q(secciones__icontains=buscar))
  cesta = Cesta.objects.filter(id=2)
  context = {
    'productos':productos,
    'cesta': cesta[0].get_productos(),
    'precio_total': cesta[0].get_total_price(),
    'busqueda':buscar,
  }
  return HttpResponse(template.render(context, request))

def cesta(request, accion='', cesta_item_id=''):
  cesta = Cesta.objects.filter(id=2)[0]
  cesta_item = CestaItem.objects.filter(id=int(cesta_item_id))[0]
  if accion == 'add':
    cesta_item.sum()
    cesta_item.save()
  elif accion == 'rm':
    cesta_item.rm()
    cesta_item.save()
  else:
    cesta.delete_cesta_item(cesta_item)
    cesta_item.delete()
  return HttpResponse(200)
 

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


def perfil(request):
  template = loader.get_template('perfil.html')
  context = {}
  return HttpResponse(template.render(context, request))

def register(request):
  template = loader.get_template('registro.html')
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"Nueva cuenta creada: {username}")
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
      return redirect("/")
    else:
      messages.error(request,"Creación fallida, sus datos son erróneos.")

  form = UserCreationForm()
  context = {'form' : form}

  return HttpResponse(template.render(context, request))

def login_phonetic(request):
  template = loader.get_template('login.html')
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"Has iniciado sesión como {username}.")
        return redirect("/")
      else:
        messages.add_message(request,messages.INFO,"Nombre de usuario o contraseña inválido.")
    else:
      messages.error(request,"Nombre de usuario o contraseña inválido.")

  form = AuthenticationForm()
  context={"login_form":form}

  return HttpResponse(template.render(context, request))

def logout_phonetic(request):
	logout(request)
	messages.info(request, "Ha cerrado sesión exitosamente.") 
	return redirect("/")