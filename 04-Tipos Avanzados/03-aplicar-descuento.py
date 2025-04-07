# Ejercicio 3: Aplicar Descuento en Promoción
#
# Descripción: En este ejercicio, además de identificar a los clientes que califican para la promoción,
# se les aplica un descuento del 10 % .
# El programa retorna:
# 1. Una lista con los IDs de los clientes que califican.
# 2. Un diccionario con los IDs de los clientes y sus montos ajustados después del descuento.
#
# Entrada: Un diccionario donde:
# Claves (str): IDs de los clientes.
# Valores (float o int): Montos de las compras.
#
# Salida: Dos elementos:
# 1. Lista de IDs de los clientes elegibles.
# 2. Diccionario con los montos ajustados.
#
# Ejemplo de uso:
# compras = {
#   'Cliente1': 200,
#   'Cliente2': 100,
#   'Cliente3': 180
# }
#
# resultado = aplicar_promocion(compras)
# print(resultado) # [['Cliente1', 'Cliente3'], {'Cliente1': 180.0, 'Cliente3': 162.0}]

print("Ejercicio 3: Aplicar Descuento en Promoción\n")

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
    Selecciona los clientes que califican para una promoción y aplica un descuento del 10%.

    :param compras: Un diccionario con los IDs de los clientes y los montos de sus compras.
    :return: Una lista con los IDs de los clientes que califican para la promoción y un diccionario con los montos ajustados.

    """
    clientes_promocion = []
    compras_ajustadas = {}
    for cliente, monto in compras.items():
        if monto >= 150:
            clientes_promocion.append(cliente)
            compras_ajustadas[cliente] = monto * 0.9
    return clientes_promocion, compras_ajustadas


resultado = aplicar_promocion(compras)
# [['Cliente1', 'Cliente3', 'Cliente4', 'Cliente6', 'Cliente8', 'Cliente9'],
# {'Cliente1': 180.0, 'Cliente3': 162.0, 'Cliente4': 135.0, 'Cliente6': 144.0, 'Cliente8': 171.0, 'Cliente9': 189.0}]
print(resultado)


# Otro ejemplo Hola Mundo!


def aplicar_promocion(compras):
    """
    Selecciona los clientes que califican para una promoción y aplica un descuento del 10%.

    :param compras: Un diccionario con los IDs de los clientes y los montos de sus compras.
    :return: Una lista con los IDs de los clientes que califican para la promoción y un diccionario con los montos ajustados.

    """
    clientes_con_promocion = [cliente for cliente,
                              monto in compras.items() if monto > 150]
    cuentas_cliente_con_promocion = {
        cliente: monto for cliente, monto in compras.items() if monto > 150}

    for cliente, monto in cuentas_cliente_con_promocion.items():
        cuentas_cliente_con_promocion[cliente] = round(monto * 0.9, 2)

        return [clientes_con_promocion, cuentas_cliente_con_promocion]
