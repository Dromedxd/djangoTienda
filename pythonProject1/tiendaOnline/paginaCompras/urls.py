from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("home", views.home, name="home"),
    path("detail/<int:producto_id>", views.detail, name="detail"),
    path("productos_por_categoria/<str:categoria>", views.productos_por_categoria, name="productos_por_categoria"),
    path("buscar/", views.buscar, name="buscar"),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('añadir_carrito/<int:producto_id>', views.añadir_al_carrito, name='añadir_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    path('pedido/', views.pedido, name='pedido'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
