import csv
import os

# Escribir un archivo CSV
with open("archivos/test.csv", "w", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)  # Instancia de la clase writer
    writer.writerow(["nombre", "apellido", "edad"])  # Encabezado
    writer.writerow(["Juan", "Pérez", 25])  # Datos fila 1
    writer.writerow(["Karla", "Gómez", 30])  # Datos fila 2

# Leer un archivo CSV
with open("archivos/test.csv", "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)  # Instancia de la clase reader
    for fila in reader:
        print(fila)
# Output:
# ['nombre', 'apellido', 'edad']
# ['Juan', 'Pérez', '25']
# ['Karla', 'Gómez', '30']

# Actualizar un archivo CSV
# Debemos crear un archivo temporal para guardar los datos
# y luego reescribir el archivo original
with open("archivos/test.csv", "r", encoding="utf-8") as r, open("archivos/test_temp.csv", "w", encoding="utf-8") as w:
    reader = csv.reader(r)  # Instancia de la clase reader del archivo original
    writer = csv.writer(w)  # Instancia de la clase writer del archivo temporal
    # Recorremos el archivo original y cuando encontramos un dato que queremos actualizar,
    # lo actualizamos en el archivo temporal con los nuevos datos
    for fila in reader:
        if fila[0] == "Juan":  # Todos los datos son strings, incluso los números
            writer.writerow(["Juan", "Pérez", 26])  # Actualizamos la edad
        else:
            writer.writerow(fila)  # Si no es Juan, escribimos la fila tal cual

# Ahora hay que eliminar el archivo original "test.csv" y renombrar "test_temp.csv" a "test.csv"
# Para ello usamos la librería os

os.remove("archivos/test.csv")
os.rename("archivos/test_temp.csv", "archivos/test.csv")
