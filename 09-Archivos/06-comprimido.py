from pathlib import Path
from zipfile import ZipFile

# Escribir en archivos comprimidos
# zip_path = Path("archivos/testing.zip")
# with ZipFile(zip_path, "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         # Agregar elementos dentro del .zip
#         # No agregar el .zip al .zip, evito un bucle infinito
#         if path != zip_path:
#             zip.write(path)  # Agregar el archivo al .zip

# con rglob itero de forma recursiva todos los archivos,
# *.* es para que me devuelva todos los archivos

# Leer archivos comprimidos
with ZipFile("archivos/testing.zip") as zip:
    # print(zip.namelist())  # Lista de archivos dentro del .zip
    info = zip.getinfo("06-comprimido.py")
    print(
        info.file_size,  # Tamaño del archivo
        info.compress_size,  # Tamaño comprimido
    )
    # Extraer todo lo que se encuentra en el archivo comprimido
    zip.extractall("archivos/extraido")
    # Extraer un archivo en específico
    zip.extract("06-comprimido.py", "archivos/extraido")
    # Extraer un archivo en específico con otro nombre
    zip.extract("06-comprimido.py", "archivos/extraido/nuevo_nombre.py")
