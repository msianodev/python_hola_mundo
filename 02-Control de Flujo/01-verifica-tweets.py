# Ejercicio 1: Verificación de Tweets
#
# Descripción:
# Este programa solicita al usuario que ingrese un tweet y
# verifica si cumple con el lı́mite de 20 caracteres.

# •Si el tweet excede los 20 caracteres,
# muestra un mensaje indicando que se ha sobrepasado el lı́mite.
# •Si el tweet tiene 20 caracteres o menos,indica que el tweet ha sido publicado.
# •No se aceptan tweets vacı́os.
#
# Variables
# •tweet(str):El tweet ingresado por el usuario.
#
# Pruebas
# 1.Entrada:
# "Hola,este es un tweet" (20caracteres).
# Salida:"Su tweet ha sido publicado".

# 2.Entrada:
# "Hola,este es un tweet muy largo"(másde20caracteres).
# Salida:"Has obrepasado el lı́mite de su publicación".

# 3.Entrada:
# ""(vacı́o).
# Salida:"No se puede publicar un tweet vacı́o”.

print("Verificación de Tweets")

tweet = input("Ingrese su tweet: ").strip().capitalize()

if len(tweet) == 0:
    print("No se puede publicar un tweet vacío")
elif len(tweet) > 20:
    print("Has sobrepasado el límite de su publicación")
else:
    print("Su tweet ha sido publicado")
