from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404 ,render, redirect
from django.http import JsonResponse
import json

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

tienda_template = 'tienda/tienda.html'
paginate = 6
def index(request):
    return render(request, 'tienda/index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if  request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'La cuenta fue creada para '+user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'cuentas/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if  request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'El usuario o la contraseña es incorrecta')
        context = {}
        return render(request, 'cuentas/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def carrito(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, created = Orden.objects.get_or_create(cliente=cliente, completo=False)
        items = orden.ordenitem_set.all()
    context = {'items':items, 'orden':orden}    
    return render(request, 'tienda/carrito.html', context)

def tienda(request):

    productos = Producto.objects.all()

    paginator = Paginator(productos, paginate)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)   

    context = {
        'page_obj':page_obj,
        'catalogos':catalogos
    }    
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
    productos={producto}
    context = {
        'productos': productos
    }
    return render(request, 'tienda/producto.html', context)

def administrador(request):    
    return render(request, 'administrador/index.html')

def updateItem(request):    
    data = json.loads(request.body)
    productId = data['productId']
    colorId = data['colorId']
    tallaId = data['sizeId']
    cantidad = data['quantity']
    action = data['action']

    color = Color.objects.get(id=colorId)
    talla = Talla.objects.get(id=tallaId)
    cliente = request.user.cliente
    product = Producto.objects.get(id=productId)
    producto_color = product.productocolor_set.get(color=color)
    producto_talla = product.productotalla_set.get(talla=talla)

    print(cliente)
    print('Action', action)
    print('Producto', product)
    print('color', color)
    print('talla', talla)
    print('producto_color', producto_color)
    print('producto_talla', producto_talla)
    print('cantidad', cantidad)

    orden, created = Orden.objects.get_or_create(cliente=cliente, completo=False)        
    ordenItem, created = OrdenItem.objects.get_or_create(orden=orden, producto=product, producto_color=producto_color, producto_talla=producto_talla)
    ordenItem
    if action == 'add':        
        ordenItem.cantidad = (ordenItem.cantidad + int(cantidad))
    elif action == 'remove':
        ordenItem.cantidad = (ordenItem.cantidad - 1)
    ordenItem.save()
    if(ordenItem.cantidad <= 0):
        ordenItem.delete()

    return JsonResponse({'quantity': orden.get_cart_items}, safe=False)

def deleteItem(request): 
    data = json.loads(request.body)    
    ordenitemId = data['ordenitemId']
    
    item = OrdenItem.objects.get(id=ordenitemId)
    item.delete()

    return JsonResponse('Item Was deleted', safe=False)
