from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('secciones/<seccion_nombre>', views.secciones, name='secciones'),
    path('producto/<int:producto_id>', views.producto, name='producto'),
    path('buscar', views.buscar, name='search'),
    path('cesta/<accion>/<int:cesta_item_id>/<int:mult>', views.cesta, name='cesta'),
    path('cesta/hide/<int:cesta_item_id>', views.cesta, name='cesta_hide'),
    path('terminos/', views.terminos, name='terminos'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('registro/', views.register, name="registro"),
    path('login/', views.login_phonetic, name="login"),
    path('logout/', views.logout_phonetic, name="logout"),
    path('checkout/', views.checkout, name="checkout"),
    path('seguimiento/', views.seguimiento, name="seguimiento"),
]
