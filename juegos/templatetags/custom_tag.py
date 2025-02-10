from django import template

register = template.Library()


@register.filter
def format_miles(value):
    try:
        return f" $ {int(value):,}".replace(",", ".")
    # cualquiera de estas dos excepciones se pueden lanzar si el valor no es un numero y si ocurre devovlemos el valor sin formatear
    except (ValueError, TypeError):
        return value
