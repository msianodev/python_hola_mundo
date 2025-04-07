from io import open

# open("nombre_archivo", "modo", "encoding")
# Modos:
# - r: lectura (default)
# - w: escritura
# - a: añadir
# - x: crear archivo
# - b: binario
# - t: texto (default)

# Escritura
texto = "hola mundo\n"

archivo = open("archivos/test-open.txt", "w", encoding="utf-8")
# Si el archivo no existe lo crea, si existe lo sobreescribe
archivo.write(texto)
archivo.close()


# Lectura
archivo = open("archivos/test-open.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()


# Lectura como lista
archivo = open("archivos/test-open.txt", "r", encoding="utf-8")
lineas = archivo.readlines()  # Lee el archivo y lo guarda en una lista
archivo.close()


# Métodos mágicos que nos devuelve la función de open()
# Trabajar con with nos permite no tener que cerrar el archivo cada vez que lo abrimos
# __enter__ se va a ejecutar al inicio del bloque with
# __exit__ se va a ejecutar al final del bloque with, cierra el archivo de forma automática
with open("archivos/test-open.txt", "r", encoding="utf-8") as archivo:
    print(archivo.readlines())  # Cargo todo el archivo en memoria
    archivo.seek(0)  # Muevo el cursor/ puntero al inicio del archivo
    for linea in archivo:   # Cargo el archivo línea por línea
        print(linea)
