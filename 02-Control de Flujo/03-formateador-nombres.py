# Ejercicio 3: Formateador de Nombres Descripción
# Este programa solicita al usuario su nombre completo y
# lo formatea eliminando espacios adicionales y capitalizando las palabras.
# Se asegura de que el usuario ingrese un nombre y un apellido válidos antes deproceder.
#
# Variables
# •nombre(str): Primer nombre del usuario.
# •segundo_nombre(str): Segundo nombre del usuario(opcional).
# •primer_apellido(str): Primera pellido del usuario.
# •segundo_apellido(str): Segundo apellido del usuario(opcional).
# •nombre_completo(str): Nombre completo concatenado y formateado.
#
# Pruebas
# 1.Entrada: "juan","carlos","perez","gomez".
# Salida: "Juan Carlos Perez Gomez".
#
# 2.Entrada: "maria","","lopez","martinez".
# Salida: "Maria Lopez Martinez".
# 3.Entrada: "nicolas","","schurmann","".
# Salida: "Nicolas Schurmann”.

print("Formateador de Nombres")
nombre = input(
    "Ingrese su primer nombre: ").strip().capitalize()
segundo_nombre = input(
    "Ingrese su segundo nombre (opcional): ").strip().capitalize()
primer_apellido = input(
    "Ingrese su primer apellido: ").strip().capitalize()
segundo_apellido = input(
    "Ingrese su segundo apellido (opcional): ").strip().capitalize()

if nombre.isalpha() and primer_apellido.isalpha():
    nombre_completo = f"{nombre} {(segundo_nombre + ' ') if segundo_nombre else ''}{
        primer_apellido} {(segundo_apellido + ' ') if segundo_apellido else ''}".strip()

    print(f"El nombre completo es: {nombre_completo}")

else:
    print("Ingrese un nombre y un apellido validos.")
