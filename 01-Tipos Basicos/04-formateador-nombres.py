# Ejercicio 4: Formateador de Nombres
#
# ¿Cómo funciona?
#
# Este programa asegura que los nombres ingresados por el usuario estén correctamente formateados.
#
# 1.Solicita al usuario los siguientes datos:
# 2.Primer nombre.
# 3.Segundo nombre(opcional).
# 4.Primer apellido.
# 5.Segundo apellido(opcional).
# 6.Elimina espacios innecesarios y capitaliza la primera letra de cada palabra.
# 7.Combina todos los nombres y apellidos en un nombre completo correctamente formateado.
#
# Entradas
# •Primer nombre, segundo nombre(opcional), primer apellido,segundo apellido(opcional).
#
# Salidas
# •Nombre completo formateado.
#
# Ejemplos
# •Entrada:"juan", "carlos", "perez" "gomez" -> Salida:"Juan Carlos Perez Gomez"
# •Entrada:"maria", "", "lopez", "martinez" -> Salida:"Maria Lopez Martinez"
# •Entrada:"nicolas","","schurmann","" -> Salida:"Nicolas Schurmann

print("Formateador de Nombres")
primer_nombre = input("Ingrese el primer nombre: ").strip().capitalize()
segundo_nombre = input(
    "Ingrese el segundo nombre(opcional): ").strip().capitalize()
primer_apellido = input("Ingrese el primer apellido: ").strip().capitalize()
segundo_apellido = input(
    "Ingrese el segundo apellido(opcional): ").strip().capitalize()

nombre_completo = f"{primer_nombre} {segundo_nombre} {
    primer_apellido} {segundo_apellido}".replace("  ", " ")

print(f"Nombre completo formateado: {nombre_completo}")
