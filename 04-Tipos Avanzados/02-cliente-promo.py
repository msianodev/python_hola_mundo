# Ejercicio 2: Seleccionar Clientes para Promoción
#
# Descripción: Este ejercicio se enfoca en identificar a los clientes que califican para una promoción.
# Los clientes califican si el monto de sus compras es mayor o igual a 150 dólares.
#
# Entrada: Un diccionario con:
# Claves (str): IDs de los clientes.
# Valores (float o int): Montos de las compras.
#
# Salida: Una lista con los IDs de los clientes que califican para la promoción.
#
# Ejemplo de uso:
# compras = {
#   'Cliente1': 200,
#   'Cliente2': 100,
#   'Cliente3': 180
# }
# clientes_promocion = aplicar_promocion(compras)
# print(clientes_promocion)  # ['Cliente1', 'Cliente3']

print("Ejercicio 2: Seleccionar Clientes para Promoción\n")

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


def aplicar_promocion(compras):
    """
    Selecciona los clientes que califican para una promoción.
    Los clientes califican si el monto de sus compras es mayor o igual a 150 dólares.
    :param compras: Un diccionario con los IDs de los clientes y los montos de sus compras.
    :return: Una lista con los IDs de los clientes que califican para la promoci
    """
    clientes_promocion = []
    for cliente, monto in compras.items():
        if monto >= 150:
            clientes_promocion.append(cliente)
    return clientes_promocion


clientes_promocion = aplicar_promocion(compras)
# ['Cliente1', 'Cliente3', 'Cliente4', 'Cliente6', 'Cliente8', 'Cliente9']
print(clientes_promocion)
