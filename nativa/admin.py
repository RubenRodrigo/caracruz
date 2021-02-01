from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Catalogo)
admin.site.register(Categoria)
admin.site.register(Color)

class ProductoImagenAdmin(admin.StackedInline):
    model = ProductoImagen

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenAdmin]

    class Meta:
        model=Producto

@admin.register(ProductoImagen)
class ProductoImagen(admin.ModelAdmin):
    pass