from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.TextField(default='Sin categoria')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.URLField()
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    productos = models.ManyToManyField('Producto', related_name='carritos')

    def __str__(self):
        return f"Carrito del usuario: {self.usuario.username}"

    def actualizar_total(self):
        total = sum(producto.precio for producto in self.productos.all())
        self.total = total
        self.save()