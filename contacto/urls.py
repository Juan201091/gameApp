from django.urls import path
from .views import *

urlpatterns = [
    path("", ContactoView.as_view(), name="contacto"),
]
