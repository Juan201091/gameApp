from django.urls import path
from .views import inicio_juegos

urlpatterns = [
    path("", inicio_juegos, name="inicio_juegos"),
]
