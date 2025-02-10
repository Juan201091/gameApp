from django.db import models
from django import forms
from django.utils.html import format_html


# Create your models here.
class Consulta(models.Model):
    contestada = "Contestada"
    Nocontestada = "No contestada"
    EnProceso = "En proceso"

    Estados = (
        (contestada, "Contestada"),
        (Nocontestada, "No contestada"),
        (EnProceso, "En proceso"),
    )
    nombre = models.CharField(max_length=10, blank=True, null=False)
    descripcion = models.TextField(blank=False, null=False)
    mail = models.EmailField(max_length=100, default="usuario@example.com")
    estado_respuesta = models.CharField(
        max_length=100, choices=Estados, default=Nocontestada
    )
    telefono = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def estado_de_respuesta(self):
        if self.estado_respuesta == "Contestada":
            # etiquetas html para cambiar el color del texto
            # estoy retornando un span con el color verde literalmente DEVUELVO LA ETIQUETA HTML Y EL CONTENIDO DE ELLA ES EL ESTADO DE LA CONSULTA
            return format_html(
                '<span style="background-color:green; color:white">{}</span>',
                self.estado_respuesta,
            )
        elif self.estado_respuesta == "No contestada":
            return format_html(
                '<span style="background-color:red; color:white">{}</span>',
                self.estado_respuesta,
            )
        elif self.estado_respuesta == "En proceso":
            return format_html(
                '<span style="background-color:orange; color:white";">{}</span>',
                self.estado_respuesta,
            )

    def save(self, *args, **kwargs):
        force_update = False
        if self.id:
            print("existo")
            force_update = True
        print("no existo")
        super().save(force_update=force_update)

    # Validacion personalizada para los campos del modelo desde la clase

    # def clean(self):
    #     # Validación personalizada para el campo mail
    #     if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", self.mail):
    #         raise ValidationError({'mail': 'El correo electrónico no es válido.'})


class Respuesta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    respuesta = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    # mapea automaticamente por clave foranea osea que obtiene la consulta al meomento de crear la instancia de la respuesta y la guarda en la base de datos no es necesario hacerlo manualmente
    def crear_respuesta(self):
        consulta_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta = "Contestada"
        consulta_cambio_estado.save()

        # envio de respuesta por mail o lo que sea

    # cuadno se eemita una respuesta del panel admin se activara el metodo save
    # cuadno se apriete el boton save de al repsuesta aqui podemos validar la logica de la respuesta
    # save se eejcuta antes de que se ejecute el metodo save del modelo aqui podemos modificar todo l oque necesitamos antes de que se ejecute el metodo save del modelo
    # campso en mayusculas o minusculas, campos que se deben llenar obligatoriamente etc
    def save(self, *args, **kwargs):
        self.crear_respuesta()
        # force_update = False  para que no cree un nuevo registro
        force_update = False
        if self.id:
            force_update = True
            # no es encesario pasar el argumento en super directaemtne esta vinculadoa a la clase
            # que lo esta heredando
            # necesario definir un metodo save para sobreescribir el metodo save de la clase padre
            # podemos ajecutar logica antes de guardar la respuesta
        super(Respuesta, self).save(force_update=force_update)
