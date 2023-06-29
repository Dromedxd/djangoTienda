from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:producto_id>", views.detail, name="detail"),
    path("productos_por_categoria/<str:categoria>", views.productos_por_categoria, name="productos_por_categoria"),
    path("buscar/", views.buscar, name="buscar"),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('carrito/', views.carrito_usuario, name='carrito'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
