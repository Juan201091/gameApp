from django.contrib import admin
from .models import Datos_Usuario

# ejemplo

# class ProductoAdmin(admin.ModelAdmin):
#     # campos visibles en el administrador mostramos las columans que quremos que se muestren
#     # segun el orden que pongamos apareceran en el administrador

#     # basico muetra los campos de la tabla en el orden que los defina e nel array
#     # fields=['categoria_id', 'fecha_publicacion', 'nombre', 'imagen']

#     # ordenado
#     fieldsets = [("Relación", {"fields":["categoria"]}),( "Datos Generales",{"fields":["fecha_publicacion","nombre","imagen","estado"]})]
admin.site.register(Datos_Usuario)
# Register your models here.
