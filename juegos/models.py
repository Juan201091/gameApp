from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.nombre


class Oferta(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Oferta de {self.juego.nombre} con {self.descuento}% de descuento"


class Reseña(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    usuario = models.ForeignKey("usuarios.Datos_Usuario", on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.PositiveIntegerField()

    def __str__(self):
        return f"Reseña de {self.juego.nombre} por {self.usuario.nombre}"
