import json
from pathlib import Path

# Escribir un archivo JSON
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1000},
    {"id": 2, "nombre": "Mouse", "precio": 20},
    {"id": 3, "nombre": "Teclado", "precio": 50},
    {"id": 4, "nombre": "Monitor", "precio": 200}
]

# Convertir a JSON, indent=4 para dar formato al archivo
data = json.dumps(productos, indent=4)  # dump escribe en un archivo
Path("archivos/productos.json").write_text(data, encoding='utf-8')

# Leer un JSON
data = Path("archivos/productos.json").read_text(encoding='utf-8')
productos = json.loads(data)  # loads lee un archivo

# Modificar un archivo JSON
productos[0]["precio"] = 1200
data = json.dumps(productos, indent=4)
Path("archivos/productos.json").write_text(data, encoding='utf-8')
# Otra forma resumida es
# Path("archivos/productos.json").write_text(json.dumps(productos, indent=4), encoding='utf-8')
