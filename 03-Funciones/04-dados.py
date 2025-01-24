# Ejercicio 4: Tirar Dados
# Este ejercicio simula el lanzamiento de un dado y calcula la frecuencia con la que aparece cada cara.
# Es perfecto para trabajar con estructuras de control y bucles.
# El siguiente código utiliza un módulo del lenguaje python para generar un número aleatorio entre 1 y 6,
# este lo veremos en mayor profundidad más adelante:
#
# import random. Esto va en la primera línea del archivo
#
# resultado = random.randint(1, 6)
# print(resultado)
#
# Puedes utilizar esta misma lı́nea de código en una función de esta manera:
# def dameNumero(desde, hasta):
# return random.randint(desde, hasta)
# print(dameNumero(1, 6))
#
# Instrucciones: Utilizando el código de más arriba,
# 1.Define una función que simule lanzar un dado múltiples veces.
# 2.Cuenta cuántas veces aparece cada cara del dado.
# 3.Calcula el porcentaje de ocurrencia de cada cara.
# 4.Maneja errores si el número de lanzamientos no es válido (por ejemplo, 0 o números negativos).
#
# Casos de ejemplo:
# Lanza un dado 10 veces
# ¿Qué porcentajes obtienes?
# Intenta lanzar un dado 0 veces.
# ¿Qué mensaje de error aparece?
# ¿Qué sucede si lanzas un dado 10000 veces?
# ¿Son los porcentajes cercanos al 16.67%?
# ¿Qué ocurre cuando lanzas el dado 1 vez?

import random

print("Ejercicio 4: Tirar Dados")


def lanzar_dado(veces):
    """
    Función que simula lanzar un dado múltiples veces.
    :param veces: Número de veces que se lanzará el dado.
    :return: Lista con los porcentajes de cada cara.
    """

    if veces <= 0:
        return "El número de lanzamientos no es válido"
    else:
        caras = [0, 0, 0, 0, 0, 0]
        for cara in range(veces):
            resultado = random.randint(1, 6)
            caras[resultado - 1] += 1
        porcentajes = [round((cara / veces) * 100, 2) for cara in caras]
        return porcentajes


print("Porcentaje de lanzar dado 10 veces: ", lanzar_dado(10))
print("Porcentaje de lanzar dado 0 veces: ", lanzar_dado(0))
print("Porcentaje de lanzar dado 10000 veces: ", lanzar_dado(10000))
