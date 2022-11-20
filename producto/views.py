from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import principal.models as models
from django.core import serializers
from django.http import JsonResponse
 
def producto(request):
  template = loader.get_template('producto.html')
  context = {
  }
  return HttpResponse(template.render(context, request))