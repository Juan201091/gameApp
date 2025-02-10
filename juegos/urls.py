from django.urls import path
from .views import inicio_juegos
from django.conf import settings

# Defino un namespace para las URLs de este archivo
# lueog en cada template puedo referenciar a una URL de este archivo con el prefijo "juegos:"
# app_name = "juegos"

urlpatterns = [
    path("", inicio_juegos, name="inicio_juegos"),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
