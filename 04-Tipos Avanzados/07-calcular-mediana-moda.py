# Ejercicio 7: Calcular Mediana y Moda
#
# Descripción: Este ejercicio calcula dos estadı́sticas importantes de una lista de números:
# 1.La mediana: Es el valor que separa la mitad superior de la mitad inferior de una lista ordenada de números.
# Si la lista tiene un número par de elementos, la mediana es el promedio de los dos valores centrales.
# 2.La moda: El valor que aparece con mayor frecuencia.
#
# Entrada: Una lista de números.
#
# Salida: La mediana y la moda de la lista.
#
# Ejemplo de uso:
# datos = [1, 2, 2, 3, 4]
# mediana, moda = calcular_mediana_y_moda(datos)
# print(mediana, moda)
#
# datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# mediana, moda = calcular_mediana_y_moda(datos)
# print(mediana, moda)
#
# Salida esperada:
# Mediana: 2, Moda: 2
# Mediana: 7, Moda: 10

print("Ejercicio 7: Calcular Mediana y Moda\n")

datos1 = [1, 2, 2, 3, 4]
datos2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calcular_mediana(numeros):
    """
    Calcula la mediana de una lista de números.
    :param numeros: Una lista de números.
    :return: La mediana de la lista.
    """
    numeros.sort()
    n = len(numeros)
    if n % 2 == 0:
        mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
    else:
        mediana = numeros[n // 2]
    return mediana


def calcular_moda(numeros):
    """
    Calcula la moda de una lista de números.
    :param numeros: Una lista de números.
    :return: La moda de la lista.
    """
    frecuencias = {numero: numeros.count(numero) for numero in numeros}
    moda = max(frecuencias, key=frecuencias.get)
    return moda


mediana = calcular_mediana(datos1)
moda = calcular_moda(datos1)

print(f"Mediana: {mediana}, Moda: {moda}")

mediana = calcular_mediana(datos2)
moda = calcular_moda(datos2)

print(f"Mediana: {mediana}, Moda: {moda}")
