# Generated by Django 4.2.2 on 2023-06-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaCompras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.TextField(default='Sin categoria'),
        ),
    ]