# Función para saber si una palabra es palíndromo
# Quitar los espacios en blanco al momento de ingrear la palabra

def palindromo(palabra):
    palabra = palabra.replace(' ', '')  # Eliminar los espacios en blanco
    palabra = palabra.lower()  # Convertir la palabra en minúsculas
    # palabra_invertida = palabra[::-1] # Invertir la palabra
    # if palabra == palabra_invertida:
    #    return True
    # else:
    #    return False
    for i in range(len(palabra)//2):
        if palabra[i] != palabra[-i - 1]:
            return False
    return True


input_palabra = input('Ingresa una palabra: ')
RESULTADO = palindromo(input_palabra)
print(f"Es palíndromo? : {RESULTADO}")

# Función de curso Hola Mundo!


def no_space(texto):
    """quitar los espacios en blanco

    Args:
        texto (string): paso un string para quitar los espacios en blanco

    Returns:
        strin: retorna un string sin espacios en blanco
    """
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    """invertir un string

    Args:
        texto (string): recibir un string para invertir

    Returns:
        string: devuelvo el string invertido
    """
    texto_invertido = ""
    for char in texto:
        texto_invertido = char + texto_invertido
    return texto_invertido


def es_palindromo(texto):
    """confirma si una palabra es palindromo

    Args:
        texto (string): recibe un string para verificar si es palindromo
    """
    texto = no_space(texto)
    texto_espejado = reverse(texto)
    return texto == texto_espejado


print("anita lava la tina: ", es_palindromo("anita lava la tina"))
print("hola mundo: ", es_palindromo("hola mundo"))
