from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
# Para leer el archivo
# Lee el archivo y lo guarda en la variable texto
texto = archivo.read_text("utf-8")

# Si quisieramos gestionar el archivo como si fuesen muchos strings debemos usar el método split
# Separa el texto por saltos de línea y los guarda en una lista
texto = archivo.read_text("utf-8").split("\n")

# Para insertar un elemento es igual como lo hacemos con las listas
texto.insert(0, "Hola mundo")

archivo.write_text("\n".join(texto), "utf-8")
