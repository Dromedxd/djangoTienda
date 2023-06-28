from django.shortcuts import render, redirect
from .models import Producto
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm
from .forms import LoginForm


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


def detail(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    context = {
        'producto': producto
    }
    return render(request, 'Paginacompras/detail.html', context)



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
            return redirect('login')  # Redirige al usuario al inicio de sesión después del registro
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
    context = {
        'productos': productos
    }
    return render(request, 'Paginacompras/productos_por_categoria.html', context)
