from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('carrito/', views.carrito, name="carrito"),
    
    path('tienda/', views.tienda, name="tienda"),
    path('tienda/<catalogo_name>/', views.tienda_catalogo, name="tienda_catalogo"),
    path('tienda/<catalogo_name>/<categoria_name>', views.tienda_categoria, name="tienda_categoria"),
    path('distribuidores/', views.distribuidores, name="distribuidores"),
    path('servicio/', views.servicio, name="servicio"),
    path('artesanos/', views.artesanos, name="artesanos"),
    path('contactos/', views.contactos, name="contactos"),
    path('producto/<int:producto_id>/', views.producto, name="producto"),
    path('administrador/', views.administrador, name="administrador"),
    path('update_item/', views.updateItem, name="updateItem"),
]
