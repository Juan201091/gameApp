from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from .forms import ConsultaForm

# Create your views here.


class ContactoView(FormView):
    # ruta a la pagina que vamos a renderizar dicho formulario
    template_name = "contacto/formulario_personalizado.html"
    # Cual es la clase administradora del formulario que vamos a utilizar en el template
    form_class = ConsultaForm
    # si el formulario es valido y se envía lo vamos a redirigir a la url especificada en el atributo success_url
    # peude ser cualquier url
    success_url = "/juegos"

    # metodo que se ejecuta cuando el formulario es valido
    # form representa la instancia del formulario que se esta utilizando ose a la instancia de ConsultaForm

    def form_valid(self, form):
        # form.save() es un metodo que vive en la clase ModelForm y se encarga de guardar los datos del formulario en la base de datos como el parametro form de esta funcion es la isntancia de ConsutlaForm entonces se guardaran los datos en la tabla Consulta
        print("heheh")
        try:
            form.save()
        except Exception as e:
            form.add_error("nombre", e)
            # renderiza fromulario nuevamente con los errores
            return self.form_invalid(form)
        # form.send_email()
        # metodo de FormView que se encarga de redirigir al usuario a la url especificada en el atributo success_url
        return super().form_valid(form)

    # validacion personalizada para el formulario desde la vista de la clase
    #  def form_valid(self, form):
    #     # Obtener los datos del formulario validado
    #     mail = form.cleaned_data.get("mail")
    #     telefono = form.cleaned_data.get("telefono")
