from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.TextField(default='Sin categoria')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class ProductoHome(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo_electronico = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.user.username
