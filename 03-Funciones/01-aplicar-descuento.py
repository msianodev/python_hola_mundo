# Ejercicio 1: Aplicar Descuento
#
# Este ejercicio tiene como objetivo ayudarte a comprender cómo calcular el total de una cuenta
# después de aplicar un descuento.
# Es ideal para practicar operaciones matemáticas simples y trabajar con funciones.
#
# Instrucciones:
# 1.Define una función que tome como parámetros el total de una cuenta
# y un porcentaje de descuento.
# 2.Calcula el monto correspondiente al descuento.
# 3.Resta el descuento del total original.
# 4.Devuelve el total final.
#
# Casos de ejemplo:
# Si tienes una cuenta de $1000 y un descuento del 20 %, el resultado debe ser $800.
# ¿Qué pasa si aplicas un descuento del 0%? ¿Y del 100%?

print("Función para aplicar descuento")


def calcular_descuento(total, descuento):
    """calculo el monto del descuento segun el total y el porcentaje de descuento

    Args:
        total (float): es el total de la cuenta que va a pagar el cliente
        descuento (float): es el porcentaje de descuento que se va a aplicar

    Returns:
        float: devuelve el monto de descuento que se va a aplicar a la cuenta en decimales
    """
    if descuento == 0:
        return total
    elif descuento < 0 or descuento > 100:
        return "Descuento no válido"
    else:
        monto_descuento = total * (descuento / 100)
        return monto_descuento


def calcular_total(total, descuento):
    """calcula el total de la cuenta despues de aplicar un descuento

    Args:
        total (float): es el total de la cuenta
        descuento (float): es el porcentaje de descuento en decimales

    Returns:
        float: devuelve el total de la cuenta despues de aplicar el descuento
    """
    return round(total - calcular_descuento(total, descuento), 2)


resultado = float(input("Ingresa el total de la cuenta: "))
descuento_obtenido = float(input("Ingresa el porcentaje de descuento: "))

print(f"El monto del descuento es: {
      calcular_descuento(resultado, descuento_obtenido)}")
print(f"El total a pagar es: {calcular_total(
    resultado, descuento_obtenido):.2f}")
