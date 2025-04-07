# Ejercicio 5: Simulación de Lanzamiento de Dados
#
# Descripción:Vamos a mejorar un ejercicio de una sección anterior,
# este ejercicio simula el lanzamiento de un dado una cantidad especı́fica de veces.
# El programa debe calcular la frecuencia de cada cara en porcentaje.
#
# Entrada:Un entero que indica cuántas veces se lanza el dado.
# Salida:Porcentaje de veces que apareció cada cara.
#
# Ejemplo de uso: tirar_dados(10)
import random

print("Ejercicio 5: Simulación de Lanzamiento de Dados\n")


def tirar_dados(lanzamientos):
    """
    Simula el lanzamiento de un dado una cantidad específica de veces.
    :param lanzamientos: Un entero que indica cuántas veces se lanza el dado.
    :return: Porcentaje de veces que apareció cada cara.
    """
    caras = [1, 2, 3, 4, 5, 6]
    frecuencias = {cara: 0 for cara in caras}
    for _ in range(lanzamientos):
        cara = random.choice(caras)
        frecuencias[cara] += 1
    for cara, frecuencia in frecuencias.items():
        print(f"Cara {cara}: {frecuencia / lanzamientos * 100:.2f}%")


tirar_dados(10)
