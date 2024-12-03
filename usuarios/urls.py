from django.urls import path
from .views import inicio_usuario

urlpatterns = [
    path("", inicio_usuario, name="inicio_usuario"),
]
