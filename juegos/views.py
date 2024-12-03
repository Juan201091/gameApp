from django.shortcuts import render


# Create your views here.
def inicio_juegos(req):
    return render(req, "juegos/inicio.html")
