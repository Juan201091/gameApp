from django.urls import path
from .views import inicio_compras

urlpatterns = [
    path("", inicio_compras, name="inicio_compras"),
]
