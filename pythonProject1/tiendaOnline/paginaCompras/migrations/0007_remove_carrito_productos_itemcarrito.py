# Generated by Django 4.2.2 on 2023-06-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paginaCompras', '0006_alter_carrito_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='productos',
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='paginaCompras.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaCompras.producto')),
            ],
        ),
    ]