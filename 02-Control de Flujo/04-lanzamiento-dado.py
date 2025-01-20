import random

# Ejercicio 4: Lanzamiento de Dado
#
# Descripción
# Simula el lanzamiento de un dado un número especificado de veces y
# calcula la frecuencia o porcentaje de cada cara.
#
# Pruebas
# 1.Lanzar el dado 10 veces.
# Salida: Porcentajes aproximados por cara.
#
# 2.Lanzar el dado 10000 veces.
# Salida:Porcentajes cercanos al 16.67% por cara.
#
# 3.Lanzar el dado 1 vez.
# Salida: Cara del dado que salió.


print("Lanzamiento de Dado")

numero_lanzamientos = int(input("¿Cuantas veces desea lanzar el dado?"))

if numero_lanzamientos <= 0:
    print("El numero de lanzamientos debe ser mayor que cero 0.")
    exit()

resultados = [0] * 6

for numero in range(numero_lanzamientos):
    cara = random.randint(1, 6)
    resultados[cara - 1] += 1  # Se resta 1 para que el indice sea 0-5

    if numero_lanzamientos == 1:
        print(f"El dado cayo en la cara {cara}")
    else:
        for i in range(6):
            procentaje = (resultados[i] / numero_lanzamientos) * 100
            print(f"Porcentaje de veces que salio la cara {
                  i + 1}: {procentaje:.2f}%")
        break
