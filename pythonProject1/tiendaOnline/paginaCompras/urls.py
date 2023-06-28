from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:producto_id>", views.detail, name="detail"),
    path("productos_por_categoria/<str:categoria>", views.productos_por_categoria, name="productos_por_categoria"),
    path("buscar/", views.buscar, name="buscar"),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
]