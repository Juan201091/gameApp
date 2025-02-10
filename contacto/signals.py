from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Consulta
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

# from .models import Usuario

# pre save se ejecuta antes de que se ejeucte el metod osave del modelo
# post save se ejecuta despues de que se ejecute el metodo save del modelo
# pre delete se ejecuta antes de que se ejecute el metodo delete del modelo
# post delete se ejecuta despues de que se ejecute el metodo delete del modelo


@receiver(post_save, sender=Consulta)
def enviar_mail(sender, instance, created, **kwargs):
    # instamce representa al instnacia que se esta guardando en la base de datos y puedo verificar si se esta creando o actualizando
    # como a su vez puedo acceder a los campos de la instancia que se esta guardando y validarlos

    if created:
        print("Se ha creado una nueva consulta")
    else:
        print("Se ha actualizado una consulta")


@receiver(pre_save, sender=Consulta)
def validar_nombre(sender, instance, **kwargs):
    if instance.nombre == "juan":
        raise ValidationError("El campo nombre ya existe")
    print("El nombre es valido")
