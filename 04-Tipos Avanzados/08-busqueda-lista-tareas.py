# Ejercicio 8: Búsqueda en Lista de Tareas
#
# Descripción: Busca tareas especı́ficas en una lista utilizando dos métodos:
# 1. Por ID.
# 2. Por texto contenido en la descripción.
#
# Entrada:
# 1. Una lista de diccionarios, donde cada diccionario tiene las claves:
# 2. 'id'(int): ID de la tarea.
# 3. 'descripcion'(str): Descripción de latarea.
# 4. Un entero para buscar por ID.
# 5. Un texto para buscar coincidencias.
#
# Salida:
# 1.La tarea que coincide con el ID.
# 2.Una lista de tareas que contien en el texto.
#
# Ejemplo de uso:
# tareas = [
#   {"id": 1, "descripcion": "Lavar los platos"},
#   {"id": 2, "descripcion": "Sacar la basura"},
#   {"id": 3, "descripcion": "Limpiar el baño"},
#   {"id": 4, "descripcion": "Hacer la cama"},
#   {"id": 5, "descripcion": "Cocinar la cena"},
#   {"id": 6, "descripcion": "Pasear al perro"},
#   {"id": 7, "descripcion": "Hacer la compra"},
#   {"id": 8, "descripcion": "Planchar la ropa"},
#   {"id": 9, "descripcion": "Regar las plantas"},
#   {"id": 10, "descripcion": "Lavar el coche"}
# ]
#
# buscar_tarea_por_id(tareas, 1)
# buscar_tareas_por_texto(tareas, "platos")
#
# Salida esperada: Tarea encontrada por ID 3:
# {'id': 3, 'descripcion': 'Limpiar el baño'}
#
# Tareas encontradas con el texto 'co':
# [
#   {'id': 5, 'descripcion': 'Cocinar la cena'},
#   {'id': 7, 'descripcion': 'Hacer la compra'},
#   {'id': 10, 'descripcion': 'Lavar el coche'}
# ]
#
# Tareas encontradas con el texto 'cO':
# [
#   {'id': 5, 'descripcion': 'Cocinar la cena'},
#   {'id': 7, 'descripcion': 'Hacer la compra'},
#   {'id': 10, 'descripcion': 'Lavar el coche'}
# ]
#
# Tareas encontradas con el texto 'almuerzo':
# []

print("Ejercicio 8: Búsqueda en Lista de Tareas\n")

tareas = [
    {"id": 1, "descripcion": "Lavar los platos"},
    {"id": 2, "descripcion": "Sacar la basura"},
    {"id": 3, "descripcion": "Limpiar el baño"},
    {"id": 4, "descripcion": "Hacer la cama"},
    {"id": 5, "descripcion": "Cocinar la cena"},
    {"id": 6, "descripcion": "Pasear al perro"},
    {"id": 7, "descripcion": "Hacer la compra"},
    {"id": 8, "descripcion": "Planchar la ropa"},
    {"id": 9, "descripcion": "Regar las plantas"},
    {"id": 10, "descripcion": "Lavar el coche"}
]


def buscar_tarea_por_id(tareas, id):
    """
    Busca una tarea específica en una lista por su ID.
    :param tareas: Una lista de diccionarios con las tareas.
    :param id: Un entero con el ID de la tarea a buscar.
    :return: La tarea que coincide con el ID.
    """
    for tarea in tareas:
        if tarea['id'] == id:
            print(f"Tarea encontrada por ID {id}:")
            print(tarea)
            return tarea
    print(f"No se encontró ninguna tarea con el ID {id}.")
    return None


def buscar_tareas_por_texto(tareas, texto):
    """
    Busca tareas en una lista por el texto contenido en la descripción.
    :param tareas: Una lista de diccionarios con las tareas.
    :param texto: Un string con el texto a buscar.
    :return: Una lista de tareas que contienen el texto.
    """
    tareas_coincidentes = []
    for tarea in tareas:
        if texto.lower() in tarea['descripcion'].lower():
            tareas_coincidentes.append(tarea)
    if tareas_coincidentes:
        print(f"Tareas encontradas con el texto '{texto}':")
        for tarea in tareas_coincidentes:
            print(tarea)
    else:
        print(f"No se encontraron tareas con el texto '{texto}'.")
    return tareas_coincidentes


buscar_tarea_por_id(tareas, 2)
buscar_tareas_por_texto(tareas, "la")
