from django.contrib import admin
from .models import Consulta, Respuesta

# Register your models here.


# admin.TabularInline es un tipo de clase que se utiliza para mostrar un formulario de un modelo en el formulario de otro modelo
class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0


# para que inlines tenga efecto este modelo administraor de la clase consulta debe ser registrado en el admin.site.register y en la propiedad inlines se le pasa la clase RespuestaInline que es la que se encarga de mostrar el formulario de Respuesta en el formulario de Consulta siemrpe y cuadno sea clave foranea


class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    # las propiedad q se vean pueden ser modificadas por metodos de la clase uqe agreguen colores personalidades etc
    list_display = [
        "estado_de_respuesta",
        "nombre",
        "descripcion",
        "mail",
        "telefono",
        "fecha",
    ]
    # se filtra por campos del modelo
    list_filter = ["estado_respuesta", "fecha"]


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ["consulta", "respuesta", "fecha"]


admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Respuesta)
