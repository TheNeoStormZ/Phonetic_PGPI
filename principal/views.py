from principal.models import Producto
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