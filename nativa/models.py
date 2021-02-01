from django.db import models

# Create your models here.
#class Cliente(models.Model):

class Catalogo(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=500, null=True)
    caracteristicas = models.CharField(max_length=1000, null=True)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="productos/", null=True)

    def __str__(self):
        return self.nombre    
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return ulr
    
class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/", null=True)

    def __str__(self):
        return self.producto.nombre
        
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return ulr


class Color(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.nombre

'''
class Orden(models.Model):
    date_orden = models.DateTimeField(auto_created=True)
    completo = models.BooleanField(default=False, null=True, blank=True)
    transaccion_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrdenItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total
'''