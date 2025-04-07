# Ejercicio 1:
# Generar un Ticket de Compra
#
# Descripción: El objetivo de este ejercicio es crear un programa
# que genere e imprima un ticket de compra a partir de una lista de productos.
# Cada producto está representado por un diccionario con un nombre y un precio.
# El programa debe calcular la cantidad de cada producto, el subtotal de cada uno y el total de la compra.
#
# Entrada: Una lista de diccionarios con las claves:
# 'nombre'(str): El nombre del producto.
# 'precio'(float):El precio del producto.
#
# Ejemplo de salida:
#
# -----------------
# Ticket de compra:
# -----------------
# Manzana   x2 - $1.00
# Pan       x1 - $1.00
# Leche     x3 - $4.50
# Galletas  x3 - $6.00
# -----------------
# Total: $12.50
# -----------------
#
# Ejemplo de uso:
#
# productos = [
#   {'nombre': 'Manzana', 'precio': 0.5},
#   {'nombre': 'Manzana', 'precio': 0.5},
#   {'nombre': 'Pan', 'precio': 1.0},
#   {'nombre': 'Leche', 'precio': 1.5}
# ]
#
# generar_ticket(productos)

print("Ejercicio 1: Generar un Ticket de Compra\n")

productos = [
    {id: 1, 'nombre': 'Manzana', 'precio': 0.5},
    {id: 2, 'nombre': 'Banana', 'precio': 0.5},
    {id: 3, 'nombre': 'Pan', 'precio': 1.0},
    {id: 4, 'nombre': 'Leche', 'precio': 1.5},
    {id: 5, 'nombre': 'Galletas', 'precio': 2.0},
    {id: 6, 'nombre': 'Cereal', 'precio': 2.5},
    {id: 7, 'nombre': 'Yogurt', 'precio': 1.0},
    {id: 8, 'nombre': 'Huevos', 'precio': 1.5},
    {id: 9, 'nombre': 'Jugo', 'precio': 1.5},
    {id: 10, 'nombre': 'Cafe', 'precio': 1.0}
]


def generar_ticket(productos):
    """
    Genera e imprime un ticket de compra a partir de una lista de productos.
    :param productos: Una lista de diccionarios con los nombres y precios de los productos.
    :return: None
    """
    total = 0
    print("-----------------")
    print("Ticket de compra:")
    print("-----------------")
    for producto in productos:
        total += producto['precio']
        print(f"{producto['nombre']} x1 - ${producto['precio']:.2f}")
    print("-----------------")
    print(f"Total: ${total:.2f}")
    print("-----------------")


generar_ticket(productos)
