# Ejercicio 2: Conversor de Unidades de Tiempo
#
# Este ejercicio te permitirá practicar cómo convertir valores entre
# diferentes unidades de tiempo.
# Es una excelente oportunidad para trabajar con estructuras condicionales
# y comprender las relaciones entre unidades de tiempo.
#
# Instrucciones:
# 1.Define tres funciones:
#   a_segundos: Convierte una cantidad y unidad dada a segundos.
#   de_segundos: Convierte una cantidad en segundos a otra unidad deseada.
#   convertir_tiempo: Usa las dos funciones anteriores para realizar una
#   conversión completa entre dos unidades.
#
# 2.Considera las siguientes unidades: segundo, minuto, hora, dı́a, mes(30dı́as), año(365dı́as).
#
# Casos de ejemplo:
# Convierte 2 horas a minutos: ¿Cuántos minutos son?
# Intenta convertir 5 lustros a años: ¿Qué mensaje de error obtienes?

print("Conversor de Unidades de Tiempo")


def a_segundos(cantidad, unidad):
    """Convierte una cantidad y unidad dada a segundos

    Args:
        cantidad (int): es la cantidad de tiempo que se va a convertir
        unidad (str): es la unidad de tiempo en la que se va a convertir

    Returns:
        int: devuelve la cantidad de tiempo en segundos
    """
    if unidad == "segundo":
        return cantidad
    elif unidad == "minuto":
        return cantidad * 60
    elif unidad == "hora":
        return cantidad * 3600
    elif unidad == "día":
        return cantidad * 86400
    elif unidad == "mes":
        return cantidad * 2592000
    elif unidad == "año":
        return cantidad * 31536000
    else:
        return "Unidad no válida"


def de_segundos(cantidad, unidad):
    """Convierte una cantidad en segundos a otra unidad deseada

    Args:
        cantidad (int): es la cantidad de tiempo en segundos que se va a convertir
        unidad (str): es la unidad de tiempo en la que se va a convertir

    Returns:
        int: devuelve la cantidad de tiempo en la unidad deseada
    """
    if unidad == "segundo":
        return cantidad
    elif unidad == "minuto":
        return cantidad / 60
    elif unidad == "hora":
        return cantidad / 3600
    elif unidad == "día":
        return cantidad / 86400
    elif unidad == "mes":
        return cantidad / 2592000
    elif unidad == "año":
        return cantidad / 31536000
    else:
        return "Unidad no válida"


def convertir_tiempo(cantidad, unidad, unidad_deseada):
    """Convierte una cantidad de tiempo de una unidad a otra

    Args:
        cantidad (float): es la cantidad de tiempo que se va a convertir
        unidad (str): es la unidad de tiempo en la que se va a convertir
        unidad_deseada (str): es la unidad a la que se va a convertir la cantidad de tiempo

    Returns:
        float: devuelve la cantidad de tiempo convertida a la unidad deseada
    """

    cantidad = float(input("Ingresa la cantidad de tiempo: "))
    unidad = input("Ingresa la unidad de tiempo: ")
    unidad_deseada = input("Ingresa la unidad a la que deseas convertir: ")

    if unidad == "segundo":
        return de_segundos(cantidad, unidad_deseada)
    else:
        return a_segundos(cantidad, unidad)


cantidad = float(input("Ingresa la cantidad de tiempo: "))
unidad = input("Ingresa la unidad de tiempo: ").lower().capitalize().strip()
unidad_deseada = input(
    "Ingresa la unidad a la que deseas convertir: ").lower().capitalize().strip()

print(f"La conversión de: {cantidad} {unidad}, son {convertir_tiempo(
    cantidad, unidad, unidad_deseada)} {unidad_deseada}")
