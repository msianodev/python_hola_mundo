from pprint import pprint
# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

# 2. Contar en un diccionario cuanto se repiten los caracteres de un string

# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista
# que contiene las tuplas [("a": 3), ("b": 2), ("c": 4 ), ("d": 4)]

# 4. De un listado de tuplas, devolver las tuplas  que tengan el mayor valor.
# [("a": 3), ("b": 2), ("c": 4 ), ("d": 4)] => [("c": 4), ("d": 4)]

# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con 4 repeticiones son:
# -C (con mayúsculas)
# -D (con mayúsculas)

# 6. Juntar la solución de los ejercicios anteriores para encontrar
# Los caracteres que más se repiten de un string


# Resolucipon
mensaje = "Hola Mundo"


def quitar_espacios(string):
    """
    Remove spaces from the given string.

    Args:
        string (str): The input string from which spaces will be removed.

    Returns:
        list: A list of characters from the input string, excluding spaces.
    """
    return [char for char in string if char != " "]


def contar_caracteres(string):
    """
    Cuenta la cantidad de veces que aparece cada carácter en una cadena dada.

    Args:
        string (str): La cadena de texto en la que se contarán los caracteres.

    Returns:
        dict: Un diccionario donde las claves son los caracteres y los valores son 
        la cantidad de veces que cada carácter aparece en la cadena.
    """
    caracteres = {}
    for char in string:
        if char in caracteres:
            caracteres[char] += 1
        else:
            caracteres[char] = 1
    return caracteres


def ordenar_por_valor(diccionario):
    """
    Ordena un diccionario por los valores de sus elementos.

    Args:
        diccionario (dict): El diccionario a ordenar.

    Returns:
        list: Una lista de tuplas que contienen las llaves y los valores del diccionario, 
        ordenadas por los valores de los elementos.
    """
    return sorted(diccionario.items(), key=lambda x: x[1], reverse=True)


def mayores_valores(tuplas):
    """
    Filtra las tuplas que tienen el mayor valor en una lista de tuplas.

    Args:
        tuplas (list): Una lista de tuplas que contienen llaves y valores.

    Returns:
        list: Una lista de tuplas que contienen las llaves y los valores más 
        altos de la lista original.
    """
    valores = [tupla[1] for tupla in tuplas]
    maximo = max(valores)
    return [tupla for tupla in tuplas if tupla[1] == maximo]


def crea_mensaje(diccionario):
    """
    Genera un mensaje a partir de un diccionario de caracteres y sus repeticiones.

    Args:
        diccionario (dict): Un diccionario donde las claves son caracteres y 
        los valores son el número de repeticiones.

    Returns:
        str: Un mensaje que indica los caracteres que más se repiten con 4 repeticiones y su conteo.
    """
    mensaje = "Los caracteres que más se repiten son:\n"
    for key, valor in diccionario.items():
        mensaje += f"-{key}\n con {valor} repeticiones\n"
    return mensaje.upper()


# ejercicio1
mensaje_sin_espacios = quitar_espacios(mensaje)
print(mensaje_sin_espacios)

# ejercicio2
caracteres_contados = contar_caracteres(mensaje)
pprint(caracteres_contados, width=1)

# ejercicio3
caracteres_ordenados = ordenar_por_valor(caracteres_contados)
print(caracteres_ordenados)

# ejercicio4
mayores = mayores_valores(caracteres_ordenados)
print(mayores)

# ejercicio5
mensaje_final = crea_mensaje(dict(mayores))
print(mensaje_final)
