from principal.models import Producto, Cesta, CestaItem
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
#import principal.models as models
 
def get_cesta(request):
  user = request.user
  if user.is_authenticated:
    cesta = Cesta.objects.filter(usuario=user)[0]
  elif Cesta.objects.filter(id=1).exists():
    cesta = Cesta.objects.filter(id=1)[0]
  else:
    cesta = Cesta.objects.create(id=1)
  return cesta

def index (request):
  productos = Producto.objects.all().values()[:6]
  cesta = get_cesta(request)
  template = loader.get_template('inicio.html')
  context = {
    'productos': productos,
    'cesta': cesta.get_productos(),
    'precio_total': cesta.get_total_price(),
    'busqueda': '',
  }
  return HttpResponse(template.render(context, request))
  
def catalogo(request):
  template = loader.get_template('catalogo.html')
  productos = Producto.objects.all().values()
  cesta = get_cesta(request)
  lista_categorias = [categoria for categoria in Producto.objects.values_list('categoria', flat=True).distinct()]
  context = {
    'productos':productos,
    'categorias':lista_categorias,
    'cesta': cesta.get_productos(),
    'precio_total': cesta.get_total_price(),
  }
  return HttpResponse(template.render(context, request))       
  
def secciones(request, seccion_nombre='Desconocido'):
  template = loader.get_template('secciones.html')
  productos = Producto.objects.filter(secciones=seccion_nombre).values()
  cesta = get_cesta(request)
  lista_secciones = [secciones for secciones in Producto.objects.values_list('secciones', flat=True).distinct()]
  context = {
    'productos':productos,
    'seccion':seccion_nombre,
    'cesta': cesta.get_productos(),
    'precio_total': cesta.get_total_price(),
  }
  return HttpResponse(template.render(context, request))      

def producto(request, producto_id=''):
  if '?' in request.get_full_path():
    lote = int(str(request.GET.get('lote', None)))
    return crear_cesta_item(request,producto_id,lote)
  template = loader.get_template('producto.html')
  producto = Producto.objects.filter(id=producto_id).values()
  cesta = get_cesta(request)
  context = {
    'producto':producto[0],
    'cesta': cesta.get_productos(),
    'precio_total': cesta.get_total_price(),
  }
  return HttpResponse(template.render(context, request))

def buscar(request):
  template = loader.get_template('inicio.html')
  buscar = request.GET.get('q', None)
  productos = Producto.objects.filter(Q(nombre__icontains=buscar) | Q(categoria__icontains=buscar) | Q(secciones__icontains=buscar))
  cesta = get_cesta(request)
  context = {
    'productos':productos,
    'cesta': cesta.get_productos(),
    'precio_total': cesta.get_total_price(),
    'busqueda':buscar,
  }
  return HttpResponse(template.render(context, request))

def cesta(request, accion='', cesta_item_id='',mult='1'):
  mult = int(mult)
  cesta = get_cesta(request)
  cesta_item = CestaItem.objects.filter(id=int(cesta_item_id))[0]
  if accion == 'add':
    cesta_item.sum(mult=mult)
    cesta_item.save()
  elif accion == 'rm':
    cesta_item.rm(mult=mult)
    cesta_item.save()
  else:
    cesta.delete_cesta_item(cesta_item)
    cesta_item.delete()
  return HttpResponse(200)

def crear_cesta_item(request, producto_id='',lote=''):
  crear_cesta_item_impl(request, producto_id='',lote=lote)
  return redirect("/producto/"+str(producto_id))

def comprar_add_cesta_item(request, producto_id='',lote=''):
  crear_cesta_item_impl(request, producto_id='',lote=lote)

def checkout(request):
  cesta = get_cesta(request)
  template = loader.get_template('checkout.html')
  context = {}
  return HttpResponse(template.render(context, request))


def crear_cesta_item_impl(request, producto_id='',lote=''):
  cesta = get_cesta(request)
  producto = Producto.objects.filter(id=producto_id)[0]
  lista_cestaitem = [item for item in cesta.get_productos() if item.producto==producto]
  if len(lista_cestaitem) == 0:
    cestaitem = CestaItem.objects.create(producto=producto,cantidad=int(lote))
  else:
    cestaitem = lista_cestaitem[0]
    cestaitem.cantidad += int(lote)
  cestaitem.save()
  cesta.add_cestaitem(cestaitem)
 

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
      cesta = Cesta.objects.create(usuario=user)
      cesta.save()
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