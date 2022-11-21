from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('secciones/<seccion_nombre>', views.secciones, name='secciones'),
    path('producto/<int:producto_id>', views.producto, name='producto'),
    path('buscar', views.buscar, name='search'),
]
