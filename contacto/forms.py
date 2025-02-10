from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField
from django.conf import settings


# clase que administrara el formulario de contacto
# MOdelForm se basa en el modelo de base de datos para el formulario
class ConsultaForm(ModelForm):
    # no esta declarado en el modelo pero se puede agregar en el formulario
    captcha = CaptchaField() if not settings.DEBUG else forms.CharField(required=False)

    class Meta:
        # especificamos el modelo que vamos a utilizar el formulario
        model = Consulta
        # definimos los campos que vamos a utilizar en el formulario de contacto como un array de strings
        fields = [
            "nombre",
            "descripcion",
            "mail",
            "telefono",
        ]
        exclude = ["captcha"]
        # Personalizacion de inputs del formulario aqui se agregan lso styles de bootstrap
        # widgets = {
        #     "nombre": forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Nombre",
        #         }
        #     ),  # clase de bootstrap
        #     "descripcion": forms.Textarea(attrs={"class": "form-control"}),
        #     "mail": forms.EmailInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "example@gmail.com",
        #         }
        #     ),
        #     "telefono": forms.NumberInput(attrs={"class": "form-control"}),
        # }
        # Personalizacion de mensajes de error del formulario en caso de que no se cumpla con las validaciones esto valadia siemrpe ocntra el modelo

    # def send_email(self):
    #     # obtenemos los datos del formulario
    #     # nombre = self.cleaned_data["nombre"] otra forma de obtener los datos del formulario
    #     nombre = self.cleaned_data.get("nombre")
    #     mail = self.cleaned_data.get("mail")
    #     descripcion = self.cleaned_data.get("descripcion")
    #     # enviamos el correo
    #     print(
    #         f"Correo enviado de {nombre} con el correo {mail} y el telefono {telefono} con el mensaje {descripcion}"
    #     )

    # Validacion personalizada para el campo mail desde la clase adminstsradora del formulario basado en el modelo consulta
    # siempre deben antepone el nombre del campo a validar con la palabra clean_
    # def clean_mail(self):
    #     mail = self.cleaned_data.get("mail")
    #     if not "@" in mail:
    #         raise forms.ValidationError("El correo debe contener '@'.")
    #     return mail

    # mensaje de validacion personalizado para validar campos debemos dejar blanck TRUE en el campo y null false ne base de datos ahi correran las validacion de los campos del formulario con los metodooos clean_

    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get("nombre")
    #     if not nombre:
    #         raise forms.ValidationError("Error debes completar el campo nombre")
    #     return nombre

    # def clean_mail(self):
    #     mail = self.cleaned_data.get("mail")
    #     if not mail:
    #         raise forms.ValidationError("Error debes completar el campo email")
    # si quiero usar validacion pernsalizda debo en el form sobreescribir el input
    # ejemplo campos de tipo charfield puedeo reliar validaciones personalizadas de todos los campos y evitar las de djo x defecto
    #     mail = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    # )
    # if "@" not in mail:
    #     raise forms.ValidationError("El correo debe contener '@'.")
    # return mail

    # estoy usando esta validacion para email acutalmente
    # opcion par que django valide el campo de tipo mail pero con un mensaje personalizado
    mail = forms.EmailField(
        error_messages={"invalid": "El correo debe contener '@' y ser válido."}
    )

    # # vinculado al metodo save de la clase asociada al formulario Conslta
    # def save(self, commit=True):
    #     # Obtener instancia del modelo antes de guardar
    #     instance = super().save(commit=False)

    #     # Aquí puedes modificar la instancia antes de guardarla
    #     instance.nombre = instance.nombre.upper()  # Convertir a mayúsculas

    #     if commit:
    #         instance.save()  # Guardar en la base de datos
    #     return instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not settings.DEBUG:
            del self.fields["captcha"]


# conclusiones crear un modelo y cada campo segun el tipo de dato que se va a almacenar
# crear un formulario basado en el modelo para administrar el formulario
# personalizar los campos del formulario con widgets en caso de no quiera modificar los errores
# en caso de querer modificar errores personalizados se debe sobreescribir el metodo clean_campo
# mensaje de validacion personalizado para validar campos debemos dejar blank TRUE en el campo y null false en base de datos ahi correran las validacion de los campos del formulario con los metodooos clean_ y podre errojar erroes personalizados en caso de que no se cumplan las validaciones no llegaran a la base de datos incluso podrai transforamr lso datos
# para correr validacion personalizadas se debe sobreescribir el campos
# esto desactiva la validacion automatica de django y permite que todo l omaneje el metodo
#  mail = forms.CharField(
#         required=True,
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "example@gmail.com"})
#     )
