from django.contrib import admin
from .models import Juego, Categoria, Oferta, Reseña
from django.shortcuts import render


class JuegosAdmin(admin.ModelAdmin):
    # este atributo sirve apra mostrar los campos del modelo en el admin cuadno ingrese a una app
    list_display = [
        "nombre",
        "categoria",
        "precio",
        "fecha_lanzamiento",
        "descripcion",
        "imagen",
    ]
    # este atributo sirve para mostrar filtrar por campos del modelo en el admin cuadno ingrese a una app
    list_filter = ["categoria", "fecha_lanzamiento"]
    # este atributo sirve para mostrar un campo de busqueda en el admin cuadno ingrese a una app
    # segurametne la clausula sql contenga un contains y retorne los resultados que contengan el valor ingresado
    search_fields = ["nombre", "descripcion"]
    # atributo que agregara un boton de accion en el admin para realizar una accion en los objetos seleccionados
    actions = ["precio_dolares", "cambiar_categoria", "selecccionados"]
    # definir funciones para el admin

    # se puede definir  dentro del modelo para encapsular su logica
    # definimos una funcion apra qque ejecute una accion en los objetos seleccionados
    def precio_dolares(self, request, queryset):
        # nombre = None
        # for obj in queryset:
        #     nombre = obj.nombre
        queryset.update(precio=8000)
        if len(queryset) == 1:
            self.message_user(
                request, f"Se cambio {len(queryset)} registro el precio a 8000"
            )
        else:
            self.message_user(
                request, f"Se cambiaron {len(queryset)} registros precios a 8000"
            )

    # como se visualiza en el admin
    precio_dolares.short_description = "Cambiar precio a 8000"

    def cambiar_categoria(self, request, queryset):
        queryset.update(categoria=1)

    def selecccionados(self, request, queryset):
        return render(request, "admin/seleccionados.html", {"queryset": queryset})


admin.site.register(Juego, JuegosAdmin)
admin.site.register(Categoria)
admin.site.register(Oferta)
admin.site.register(Reseña)
# Register your models here.
