# Ejercicio 6: Filtrar y Mostrar Cursos por Estado
#
# Descripción: Este ejercicio organiza una lista de cursos en tres grupos según su estado:
# 1. En progreso.
# 2. Completados.
# 3. No iniciados.
#
# El programa debe mostrar cada grupo con un tı́tulo correspondiente.
#
# Entrada: Una lista de diccionarios, donde cada diccionario tiene las claves:
# 'nombre'(str): Nombre del curso.
# 'estado'(str): Estado del curso.
#
# Salida:Tres listas separadas según el estado de los cursos.
#
# Ejemplo de uso:
# cursos = [
#   {"nombre": "HTML: Sin Fronteras", "estado": "en progreso"},
#   {"nombre": "CSS3: Sin Fronteras", "estado": "completado"},
#   {"nombre": "SQL: Sin Fronteras", "estado": "no iniciado"},
#   {"nombre": "Python: HTML, CSS, Flask, MySQL", "estado": "en progreso"},
#   {"nombre": "Aprende Javascript, HTML5, CSS3 y NodeJS desde cero", "estado": "completado"},
#   {"nombre": "React - Guía definitiva: hooks, router, redux, next + Proyectos","estado": "no iniciado"},
#   {"nombre": "TypeScript: sin fronteras", "estado": "completado"},
#   {"nombre": "Ultimate Python", "estado": "en progreso"},
#   {"nombre": "Ultimate Linux", "estado": "completado"},
#   {"nombre": "Ultimate Docker", "estado": "no iniciado"},
#   {"nombre": "Ultimate GIT + GITHUB", "estado": "en progreso"},
#   {"nombre": "Ultimate JavaScript", "estado": "completado"},
#   {"nombre": "Ultimate React", "estado": "no iniciado"},
#   {"nombre": "Ultimate Java", "estado": "en progreso"}
# ]
#
# mostrar_cursos_por_estado(cursos)
#
# salida_esperada =
#
# Cursos en Progreso:
# - HTML: Sin Fronteras
# - Python: HTML, CSS, Flask, MySQL
# - Ultimate Python
# - Ultimate GIT + GITHUB
# - Ultimate Java
#
# Cursos Completados:
# - CSS3: Sin Fronteras
# - Aprende Javascript, HTML5, CSS3 y NodeJS desde cero
# - TypeScript: sin fronteras
# - Ultimate Linux
# - Ultimate JavaScript
#
# Cursos No Iniciados:
# - SQL: Sin Fronteras
# - React
# - Guía definitiva: hooks, router, redux, next + Proyectos
# - Ultimate Docker
# - Ultimate React

print("Ejercicio 6: Filtrar y Mostrar Cursos por Estado\n")

cursos = [
    {"nombre": "HTML: Sin Fronteras", "estado": "en progreso"},
    {"nombre": "CSS3: Sin Fronteras", "estado": "completado"},
    {"nombre": "SQL: Sin Fronteras", "estado": "no iniciado"},
    {"nombre": "Python: HTML, CSS, Flask, MySQL", "estado": "en progreso"},
    {"nombre": "Aprende Javascript, HTML5, CSS3 y NodeJS desde cero",
        "estado": "completado"},
    {"nombre": "React - Guía definitiva: hooks, router, redux, next + Proyectos",
        "estado": "no iniciado"},
    {"nombre": "TypeScript: sin fronteras", "estado": "completado"},
    {"nombre": "Ultimate Python", "estado": "en progreso"},
    {"nombre": "Ultimate Linux", "estado": "completado"},
    {"nombre": "Ultimate Docker", "estado": "no iniciado"},
    {"nombre": "Ultimate GIT + GITHUB", "estado": "en progreso"},
    {"nombre": "Ultimate JavaScript", "estado": "completado"},
    {"nombre": "Ultimate React", "estado": "no iniciado"},
    {"nombre": "Ultimate Java", "estado": "en progreso"}
]


def mostrar_cursos_estado(cursos):
    """
    Organiza una lista de cursos en tres grupos según su estado.
    :param cursos: Una lista de diccionarios con los nombres y estados de los cursos.
    :return: Tres listas separadas según el estado de los cursos.
    """
    # Usando el método de filter
    en_progreso = filter(
        lambda curso: curso['estado'] == 'en progreso', cursos)

    # Usando una comprensión de listas
    completados = [
        curso for curso in cursos if curso['estado'] == 'completado']
    no_iniciados = [
        curso for curso in cursos if curso['estado'] == 'no iniciado']

    return en_progreso, completados, no_iniciados


def mostrar_cursos(cursos, titulo):
    """
    Imprime una lista de cursos con un título.
    :param cursos: Una lista de diccionarios con los nombres de los cursos.
    :param titulo: Un string con el título de la lista de cursos.
    :return: None
    """
    print(f"{titulo}:")
    for curso in cursos:
        print(f"- {curso['nombre']}")
    print()


def mostrar_curso_por_estado(cursos):
    """
    Muestra los cursos organizados por estado.
    :param cursos: Una lista de diccionarios con los nombres y estados de los cursos.
    :return: None
    """
    en_progreso, completados, no_iniciados = mostrar_cursos_estado(cursos)
    mostrar_cursos(en_progreso, "Cursos en Progreso")
    mostrar_cursos(completados, "Cursos Completados")
    mostrar_cursos(no_iniciados, "Cursos No Iniciados")


mostrar_curso_por_estado(cursos)
