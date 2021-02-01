from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'tienda/index.html')

def tienda(request):

    '''
    catalogo = Catalogo.objects.get(nombre="Damas")
    categorias = Categoria.objects.filter(catalogo=catalogo)
    productos = []
    for categoria in categorias:
        productos.append(Producto.objects.filter(categoria=categoria))
    '''
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'productos':productos,
        'categorias':categorias
    }
    return render(request, 'tienda/tienda.html', context)

def distribuidores(request):
    return render(request, 'tienda/distribuidores.html')

def servicio(request):
    return render(request, 'tienda/servicio.html')

def artesanos(request):
    return render(request, 'tienda/artesanos.html')

def contactos(request):
    return render(request, 'tienda/contactos.html')

def producto(request, producto_id):
    return render(request, 'tienda/producto.html')