from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Datos_Usuario(models.Model):
    # no es necesario agregar un campo id para identficar los registros, ya que Django lo crea automáticamente con ONE TO ONE
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    documento = models.CharField(max_length=10)
    cuil = models.CharField(max_length=10)
    imagen = models.ImageField(
        upload_to="usuario/%Y/%m/%d",
        default="defecto/defecto.png",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username


class Biblioteca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    juego = models.ForeignKey("juegos.Juego", on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=50,
        choices=[("adquirido", "Adquirido"), ("jugado", "Jugado")],
        default="adquirido",
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.nombre}"
