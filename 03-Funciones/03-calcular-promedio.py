# Ejercicio 3: Calcular Promedio
#
# En este ejercicio aprenderá a calcular el promedio de una serie de números.
# También trabajarás con parámetros variables en funciones.
#
# Instrucciones:
# 1.Define una función que acepte un número variable de argumentos.
# 2.Si no se proporcionan números, devuelve 0.
# 3.Si se proporcionan números, calcula y devuelve el promedio.
#
# Casos de ejemplo:
# Calcula el promedio de los números 1, 2, 3, 4, 5
# ¿Qué sucede si no proporcionas ningún número?

print("Calcular Promedio")


def calcular_promedio(*args):
    """Calcula el promedio de una serie de números

    Args:
        *args (int): es una serie de números

    Returns:
        float: devuelve el promedio de los números
    """
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)


total1 = calcular_promedio(1, 2, 3, 4, 5)  # 3.0
total2 = calcular_promedio()  # 0
total3 = calcular_promedio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 5.5

print(f'El promedio de los números 1, 2, 3, 4, 5 es: {total1}')
print(f'El promedio de los números vacios en argumento es:', {total2})
print(
    f'El promedio de los números 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 es:', {total3})
