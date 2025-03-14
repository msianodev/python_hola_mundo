import sys
from pathlib import Path
import os

# print(sys.argv)  # ['11-Paquetes Nativos/01-cli.py']
# Nos devuelve una lista con los argumentos que le pasamos al script


def cli(args):
    # valido si tiene algun argumento por parámetro
    if len(args) == 1:
        print('No hay argumentos')
        return
    # Preguntar si tiene 1 o más argumentos
    if len(args) != 3:
        print('Se necesita 2 argumentos')
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print(f'Ruta de origen no existe: {origen}')
        return

    destino = args[2]
    d = Path(destino)
    if not d.exists():
        print(f'Ruta de destino no existe: {destino}')
        return

    # Funcionalidad para renombar archivos
    os.rename(str(origen), str(destino))
    print(f'Archivo {origen} renombrado a {destino}')


cli(sys.argv)  # ['11-Paquetes Nativos/01-cli.py']
