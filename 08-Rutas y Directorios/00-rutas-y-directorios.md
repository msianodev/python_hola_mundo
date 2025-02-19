# Rutas y directorios

# **Definición y Ejemplo Sencillo**

Las rutas en Python son direcciones que apuntan a archivos o carpetas dentro del sistema de archivos. Se pueden manejar de dos formas:

- **Rutas absolutas**: Indican la ubicación completa de un archivo o directorio desde la raíz del sistema.
- **Rutas relativas**: Indican la ubicación en relación con el directorio actual.

```python
from pathlib import Path

Path(r"C:/Users/Usuario/archivo.txt") # En windows se usa la r adelante para indicar ruta

path = Path("curso-python/mi-archivo.py")

# Métodos de la clase Path
path.is_file() # Verifica si es un archivo
path.is_dir() # Verifica si es un directorio
path.exists() # Verifica si existe la ruta

# Propiedades de la clase Path
print(
	path.name, # Output: El nombre del archivo incluyendo su extensión: mi-archivo.py
	path.stem, # Output: El nombre del archivo sin su extensión: mi-archivo
	path.suffix, # Output: La extensión: .py
	path.parent, # Output: Directorio padre: curso-python
	path.absolute() # Output: La ruta absoluta desde la raíz hasta el archivo con extension
)
```

Ejemplo sencillo:

```python
import os

# Ruta absoluta
ruta_absoluta = "C:/Users/Usuario/archivo.txt"

# Ruta relativa
ruta_relativa = "./archivo.txt"

print(os.path.abspath(ruta_relativa))  # Convierte relativa en absoluta

```

---

# **Directorios**

Python proporciona el módulo `os` y `pathlib` para trabajar con directorios.

Ejemplo de manipulación de directorios:

```python
import os

# Crear un directorio
os.mkdir("mi_carpeta")

# Listar archivos en un directorio
print(os.listdir("."))

# Eliminar un directorio vacío
os.rmdir("mi_carpeta")

```

```python
from pathlib import Path

path = Path("directorio")
path.exists() # Output: Verifica si existe
path.mkdir() # Output: Crea la carpeta o directorio
path.rmdir() # Output: Elimina el directorio (vacío unicamente)
path.rename("test") # Output: Cambia el nombre del directorio
```

**Iterar y renombrar archivos en una carpeta**

```python
from pathlib import Path

# Carpeta donde están los archivos
directorio = Path("mi_carpeta")

# Iterar sobre los archivos dentro del directorio
for archivo in directorio.iterdir():
    if archivo.is_file():  # Verificar que es un archivo
        nuevo_nombre = archivo.parent / f"nuevo_{archivo.name}"
        archivo.rename(nuevo_nombre)

print("Archivos renombrados exitosamente.")

# Utilizando listas de comprensión exclusivas de python:
archivos = [p for p in path.iterdir() if not p.is_dir()]
```

**Diferencias clave en este ejemplo:**

- `Path("mi_carpeta")` crea un objeto de ruta, en lugar de manejar cadenas.
- `.iterdir()` permite recorrer archivos y carpetas en la ruta dada.
- `.parent / "nuevo_" + archivo.name` construye la nueva ruta sin concatenar cadenas manualmente.

### Seleccionar archivos que cumplan con un patrón

```python
from pathlib import Path

path = Path("rutas")

archivos = [p for p in path.glob("*.py")]
# Trae todos los archivos que tengan la extensión .py del directorio buscado
print(archivos)
```

### Recursivas dentro de todas las carpetas

```python
from pathlib import Path

path = Path("rutas")

archivos = [p for p in path.glob("**/*.py")]
# Trae todos los archivos que tengan la extensión .py del directorio buscado
# Otra alternativa recursiva:
archivos = [p for p in path.rglob("*.py")]
print(archivos)
```

---

# **Inyección de Dependencias**

La **inyección de dependencias** (Dependency Injection, DI) es un **patrón de diseño** que permite **pasar las dependencias como parámetros en lugar de crearlas dentro de una clase**. Esto hace que el código sea más **modular, reutilizable y fácil de probar**.

### 🔹 **Ejemplo sin inyección de dependencias (Código acoplado)**

Aquí tenemos una clase `Cliente` que depende directamente de la clase `Servicio`. El problema es que `Cliente` crea una instancia de `Servicio` dentro de sí misma, lo que **hace difícil cambiar o reemplazar `Servicio` sin modificar `Cliente`**.

```python
class Servicio:
    def operar(self):
        return "Ejecutando servicio"

class Cliente:
    def __init__(self):
        self.servicio = Servicio()  # ❌ CREANDO la dependencia dentro de la clase

    def ejecutar(self):
        return self.servicio.operar()

# Uso
cliente = Cliente()
print(cliente.ejecutar())  # "Ejecutando servicio"

```

### 🔹 **Problema con este código:**

1. `Cliente` está **acoplado** a `Servicio`, lo que hace difícil modificar o reemplazar `Servicio` sin cambiar `Cliente`.
2. No podemos reutilizar `Cliente` con otra implementación de `Servicio` (por ejemplo, un `ServicioMock` para pruebas).
3. Es más difícil hacer **testing**, porque no podemos inyectar una versión falsa de `Servicio`.

---

### **✅ Solución: Inyección de Dependencias**

En este nuevo enfoque, pasamos `Servicio` como un **parámetro en el constructor**, lo que permite mayor flexibilidad.

```python
class Servicio:
    def operar(self):
        return "Ejecutando servicio"

class Cliente:
    def __init__(self, servicio):  # ✅ Recibe el servicio como dependencia
        self.servicio = servicio

    def ejecutar(self):
        return self.servicio.operar()

# Uso normal
servicio_real = Servicio()
cliente = Cliente(servicio_real)
print(cliente.ejecutar())  # "Ejecutando servicio"

```

### **🛠️ Ventajas de este enfoque:**

✔ **Desacoplamiento**: `Cliente` ya no está atado a una implementación específica de `Servicio`.

✔ **Reutilización**: Podemos cambiar `Servicio` por otra implementación sin tocar `Cliente`.

✔ **Fácil testing**: Podemos inyectar un servicio falso (`Mock`) para pruebas unitarias.

---

### **🔹 Ejemplo con un servicio de prueba (Mock)**

Si queremos probar `Cliente` sin depender de `Servicio`, podemos crear un **mock** (una versión falsa de `Servicio`) y pasarlo a `Cliente`:

```python
class ServicioMock:
    def operar(self):
        return "Servicio de prueba"

# Inyectamos el servicio falso en Cliente
servicio_mock = ServicioMock()
cliente = Cliente(servicio_mock)

print(cliente.ejecutar())  # "Servicio de prueba"

```

✅ Ahora `Cliente` funciona con cualquier clase que implemente `operar()`, sin depender de una implementación específica.

---

### **📌 Conclusión**

🔹 Sin inyección de dependencias: `Cliente` está **acoplado** a `Servicio` y no es reutilizable.

🔹 Con inyección de dependencias: `Cliente` es más **modular**, **reutilizable** y **fácil de testear**.

---