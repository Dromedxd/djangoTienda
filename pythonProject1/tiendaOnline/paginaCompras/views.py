from django.shortcuts import render, redirect
from .models import Producto, Carrito, ItemCarrito,RegistroCompra
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm
from .forms import LoginForm
from django.core.exceptions import ObjectDoesNotExist




def home(request):
    username = request.user.username
    productos = Producto.objects.all()
    categorias = Producto.objects.values('categoria').distinct()

    context = {
        'productos': productos,
        'categorias': categorias,
        'username': username,
    }
    return render(request, 'Paginacompras/home.html', context)

def buscar(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(Q(nombre__icontains=query))
    context = {
        'productos': productos
    }
    return render(request, 'Paginacompras/buscar.html', context)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'Paginacompras/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'Paginacompras/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def productos_por_categoria(request, categoria):
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Producto.objects.values('categoria').distinct()
    context = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'Paginacompras/productos_por_categoria.html', context)


def detail(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    context = {
        'producto': producto
    }
    return render(request, 'Paginacompras/detail.html', context)


def ver_carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
    except ObjectDoesNotExist:
        carrito = Carrito.objects.create(usuario=request.user)

    carrito.calcular_total()  # Calcular el precio total del carrito

    return render(request, 'Paginacompras/carrito.html', {'carrito': carrito})


def añadir_al_carrito(request, producto_id):
    if request.method == 'POST':
        cantidad = request.POST.get('quantity')
        if cantidad is not None:
            producto = Producto.objects.get(id=producto_id)
            carrito = Carrito.objects.get(usuario=request.user)
            try:
                item = ItemCarrito.objects.get(carrito=carrito, producto=producto)
                item.cantidad += int(cantidad)
            except ItemCarrito.DoesNotExist:
                item = ItemCarrito(carrito=carrito, producto=producto, cantidad=int(cantidad))

            item.save()

    return redirect('detail', producto_id=producto_id)


def vaciar_carrito(request):
    if request.method == 'POST':
        carrito = Carrito.objects.get(usuario=request.user)
        carrito.items.all().delete()
    return redirect('ver_carrito')







def confirmar_compra(request):
    if request.method == 'POST':
        carrito = Carrito.objects.get(usuario=request.user)

        contenido_carrito = ""
        for item in carrito.items.all():
            contenido_carrito += f"{item.producto.nombre} - Cantidad: {item.cantidad}\n"

        # Obtener el total del carrito
        total_carrito = carrito.total

        # Crear el registro de compra con el contenido y el total del carrito
        registro = RegistroCompra.objects.create(usuario=request.user, contenido_carrito=contenido_carrito, total=total_carrito)

        carrito.items.all().delete()

        return redirect('pedido')

    elif request.method == 'GET':
        return redirect('ver_carrito')

def pedido(request):
    registro_compra = RegistroCompra.objects.filter(usuario=request.user).last()
    contenido_carrito = ""
    if registro_compra:
        contenido_carrito = registro_compra.contenido_carrito

    context = {
        'contenido_carrito': contenido_carrito,
        'registro_compra': registro_compra,  # Agrega este campo al contexto
    }
    return render(request, 'Paginacompras/pedido.html', context)
