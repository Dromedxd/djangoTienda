from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'Paginacompras/home.html', context)


def detail(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    context = {
        'producto': producto
    }
    return render(request, 'Paginacompras/detail.html', context)