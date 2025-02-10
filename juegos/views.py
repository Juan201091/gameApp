from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.
def inicio_juegos(req):
    productos = Juego.objects.all()
    print(productos[0].descripcion)
    return render(req, "juegos/inicio.html", {"juegos": productos})
