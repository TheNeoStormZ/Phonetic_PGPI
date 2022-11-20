from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto, name='producto'),
]
