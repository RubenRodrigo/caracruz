from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404 ,render

from .models import *
# Create your views here.
tienda_template = 'tienda/tienda.html'
paginate = 6
def index(request):
    return render(request, 'tienda/index.html')

def tienda(request):

    productos = Producto.objects.all()

    paginator = Paginator(productos, paginate)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)   

    context = {
        'page_obj':page_obj,
        'catalogos':catalogos
    }
    print(context)
    return render(request, tienda_template, context)

def tienda_catalogo(request, catalogo_name):
    catalogo = get_object_or_404(Catalogo, nombre=catalogo_name)
        
    productos = catalogo.producto_set.all()

    paginator = Paginator(productos, paginate)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'catalogo':catalogo,
        'catalogos':catalogos,
        'page_obj':page_obj
    }
    return render(request, tienda_template, context)

def tienda_categoria(request, catalogo_name, categoria_name):
    catalogo = get_object_or_404(Catalogo, nombre=catalogo_name)
    categoria = get_object_or_404(Categoria, nombre=categoria_name)
        
    productos = categoria.producto_set.all()

    paginator = Paginator(productos, paginate)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'catalogo':catalogo,
        'catalogos':catalogos,
        'page_obj':page_obj
    }
    return render(request, tienda_template, context)


def catalogos():
    catalogos = Catalogo.objects.all()
    catalogo_categorias = []
    for catalogo in catalogos:
        catalogo_categorias.append(
            {
                'nombre': catalogo.nombre,
                'categorias':catalogo.categoria_set.all(),
            }
        ) 
    return catalogo_categorias  


def distribuidores(request):
    return render(request, 'tienda/distribuidores.html')

def servicio(request):
    return render(request, 'tienda/servicio.html')

def artesanos(request):
    return render(request, 'tienda/artesanos.html')

def contactos(request):
    return render(request, 'tienda/contactos.html')

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    productos=[producto]
    context = {
        'productos': productos
    }
    return render(request, 'tienda/producto.html', context)