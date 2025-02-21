from pathlib import Path
from time import ctime

archivo = Path("archivo/archivo-prueba.txt")

print(archivo.stat())  # Información del archivo

# Output: os.stat_result(
# st_mode=33206, # Tipo de archivo y permisos
# st_ino=1125899906842625, # Número de inodo
# st_dev=4195380, # Número de dispositivo
# st_nlink=1,   # Número de enlaces
# st_uid=0,     # ID del usuario
# st_gid=0,     # ID del grupo
# st_size=0, # Tamaño del archivo
# st_atime=1620000000, # Fecha de último acceso
# st_mtime=1620000000, # Fecha de última modificación
# st_ctime=1620000000 # Fecha de creación para windows, y última modificación para linux o mac
#  )
print("acceso", archivo.stat().st_atime)
# Output: acceso 1739973841.6534686 Fecha de último acceso.
# Timestamp: la fecha que tiene el archivo con respecto al 01 de enero de 1970.
# Es una fecha UNIX, este formato se ve trabajado en linux y macOS)

# Para convertirlo a una fecha legible debemos usar la librería time el método ctime
print("acceso", ctime(archivo.stat().st_atime))
# Output: acceso Wed Feb 19 11:04:01 2025
print("creación", ctime(archivo.stat().st_ctime))
# Output: creación Wed Feb 19 11:03:26 2025
print("modificación", ctime(archivo.stat().st_mtime))
# Output: modificación Wed Feb 19 11:04:01 2025
