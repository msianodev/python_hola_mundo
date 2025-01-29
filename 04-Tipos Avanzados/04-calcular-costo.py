# Ejercicio 4: Calcular el Costo Total de la Promoción
#
# Descripción: Este ejercicio calcula el costo total de la promoción,
# es decir, la suma de los descuentos aplicados a los clientes elegibles.
#
# Entrada: Un diccionario con:
# •Claves (str): IDs de los clientes.
# •Valores(float o int): Montos de las compras.
#
# Salida: Un número que representa el costo total de los descuentos aplicados.
#
# Ejemplo de uso:
# compras = {
#   'Cliente1': 200,
#   'Cliente2': 100,
#   'Cliente3': 180
# }
#
# costo_promocion = calcular_costo_promocion(compras)
# print(costo_promocion) # 38.0

print("Ejercicio 4: Calcular el Costo Total de la Promoción\n")

compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180,
    'Cliente4': 150,
    'Cliente5': 50,
    'Cliente6': 160,
    'Cliente7': 140,
    'Cliente8': 190,
    'Cliente9': 210,
    'Cliente10': 130
}


def calcular_costo_promocion(compras):
    """
    Calcula el costo total de la promoción, es decir, la suma de los descuentos aplicados a los clientes elegibles.
    :param compras: Un diccionario con los IDs de los clientes y los montos de sus compras.
    :return: Un número que representa el costo total de los descuentos aplicados.
    """
    clientes_promocion = []
    costo_promocion = 0
    for cliente, monto in compras.items():
        if monto >= 150:
            clientes_promocion.append(cliente)
            costo_promocion += monto * 0.1
    return costo_promocion


costo_promocion = calcular_costo_promocion(compras)
print(costo_promocion)
