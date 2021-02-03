from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tienda', views.tienda, name="tienda"),
    path('distribuidores/', views.distribuidores, name="distribuidores"),
    path('servicio/', views.servicio, name="servicio"),
    path('artesanos/', views.artesanos, name="artesanos"),
    path('contactos/', views.contactos, name="contactos"),
    path('producto/<int:producto_id>/', views.producto, name="producto"),
]
