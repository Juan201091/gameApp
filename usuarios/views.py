from django.shortcuts import render


# Create your views here.
def inicio_usuario(req):
    return render(req, "usuarios/inicio.html")
