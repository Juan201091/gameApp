from django.db import models
from usuarios.models import User  # Relacionado con la app usuarios


class Compra(models.Model):
    # si no especifico el cmapo id co nel tipo de dato que quiero django lo creará e interpreta como un campo autoincremental
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros detalles de la compra...

    def __str__(self):
        return f"Compra {self.id} por {self.usuario.username}"


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    juego = models.ForeignKey(
        "juegos.Juego", on_delete=models.CASCADE
    )  # Relación con la app juegos
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de compra {self.compra.id} - Juego {self.juego.nombre}"
