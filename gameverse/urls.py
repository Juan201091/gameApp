"""
URL configuration for gameverse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from compras.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("captcha/", include("captcha.urls")),
    path("", inicio_compras),
    path("accounts/", include("registration.backends.default.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("juegos/", include("juegos.urls")),
    path("medios_pagos/", include("medios_pagos.urls")),
    path("compras/", include("compras.urls")),
    path("contacto/", include("contacto.urls")),
]

# Solo si estamos en modo DEBUG
if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    # Agregar rutas de debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

    # Servir archivos multimedia (MEDIA_ROOT) durante el desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
