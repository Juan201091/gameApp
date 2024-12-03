from django.shortcuts import render


# Create your views here.
def inicio_compras(req):
    return render(req, "compras/inicio.html")
