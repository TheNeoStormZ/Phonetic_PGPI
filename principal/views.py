from principal.models import Producto, Cesta, CestaItem, Pedido, EstadoPedido
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import View
from django.http import JsonResponse
import stripe
from phonetic import settings
from django.views.decorators.csrf import csrf_protect
#import principal.models as models
 
def get_cesta(request):
  user = request.user
  if user.is_authenticated:
    if Cesta.objects.filter(usuario=user).exists():
      cesta = Cesta.objects.filter(usuario=user)[0]
    else:
      cesta = Cesta.objects.create(usuario=user)
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

def seguimiento(request, pedido_id):
  cesta = get_cesta(request)
  template = loader.get_template('seguimiento.html')
  context = {
    'cesta': cesta.get_productos(),
    'precio_total': cesta.get_total_price(),
    'busqueda': '',
  }
  if Pedido.objects.filter(id = pedido_id).all().exists():
    pedido = Pedido.objects.filter(id = pedido_id).all()[0]
    context = {
      'cesta': cesta.get_productos(),
      'precio_total': cesta.get_total_price(),
      'busqueda': '',
      'pedido':pedido,
    }
  else:
    messages.error(request, 'No existe el pedido')
  

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
    if  'comprar' in request.get_full_path():
      return checkout(request,producto_id,lote)
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
  crear_cesta_item_impl(request, producto_id=producto_id,lote=lote)
  return redirect("/producto/"+str(producto_id))

def checkout(request, producto_id="",lote=""):
  cesta = get_cesta(request)
  for cestaitem in cesta.get_productos():
    stock = cestaitem.producto.stock
    if (cestaitem.cantidad>stock):
      cestaitem.cantidad = stock
      cestaitem.save()
  amount = int(cesta.get_total_price()*100)
  if request.method == 'POST':
    return stripe_pago(request, amount)
  if not(producto_id=="" and lote==""):
    crear_cesta_item_impl(request, producto_id=producto_id,lote=lote)
    return 0
  else:
    template = loader.get_template('checkout.html')
    context = {
      'cesta': cesta.get_productos(),
      'precio_total': cesta.get_total_price(),
      'busqueda': '',
      'STRIPE_PUBLIC_KEY':settings.STRIPE_PUBLIC_KEY,
      'amount': amount,
    }
    return HttpResponse(template.render(context, request))
  

def lista_pedidos(request):
  cesta = get_cesta(request)
  buscar = request.GET.get('p', None)
  if buscar is None:
    user = request.user
    template = loader.get_template('lista_pedidos.html')
    context = {}
    if user.is_authenticated:
      pedidos_entregados = Pedido.objects.filter(usuario=user,estado=EstadoPedido.ENT.value).all()
      pedidos_pendientes = Pedido.objects.filter(usuario=user,estado=EstadoPedido.PEND).all()
      context = {
        'pedidos_entregados':pedidos_entregados,
        'pedidos_pendientes':pedidos_pendientes,
        'estado_entregado':EstadoPedido.ENT.value,
        'user':user,
        'cesta': cesta.get_productos(),
        'precio_total': cesta.get_total_price(),
      }
    return HttpResponse(template.render(context, request))
  else: 
    return redirect("/seguimiento/"+ str(buscar))


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

def cancelar_pedido(request, pedido_id):
  pedido = Pedido.objects.filter(id=pedido_id)[0]
  pedido.delete()
  messages.info(request, "Pedido cancelado.")
  return redirect("/pedidos")

@csrf_protect
def stripe_pago(request, amount):
  # Obtén la información de pago del formulario enviado
  token = request.POST.get('stripeToken')
  direccon = request.POST.get('lugar')
  plazo = request.POST.get('gridRadios')


  # Configura la clave secreta de Stripe
  stripe.api_key = settings.STRIPE_SECRET_KEY

  # Crea un cargo en Stripe
  try:
      charge = stripe.Charge.create(
          amount=amount,
          currency='eur',
          description='Phonetic - Pago',
          source=token,
      )
      print("Pago completado")
      user = request.user
      cesta = get_cesta(request)
      pedido = Pedido.objects.create(usuario=user, estado=EstadoPedido.PEND, lugar=direccon, plazo=int(plazo))
      print(cesta.get_productos())
      pedido.cestaItem.set(cesta.get_productos())
      cesta.items.set([])
      pedido.save()
      cesta.save()
  except stripe.error.CardError as e:
      # La tarjeta fue rechazada
      pass

  # Devuelve una respuesta al navegador
  return redirect("/pedidos")
