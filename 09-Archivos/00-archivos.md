# Archivos

### Archivos en Python

Los archivos en Python permiten almacenar y manipular datos de forma persistente en disco. Se pueden leer, escribir y modificar utilizando funciones específicas del lenguaje.

### Métodos de manipulación de archivos

```python
archivo.exist() # verifica que el archivo existe
archivo.rename() # cambiar el nombre al archivo
archivo.unlink() # eliminar el archivo
archivo.stat() # muestra las estadisticas del archivo
```

### Lectura y Escritura de Archivos

Python usa la función `open()` para abrir archivos. Este método acepta el nombre del archivo y el modo en el que se abrirá:

- `'r'` → Solo lectura.
- `'w'` → Escritura (crea o sobrescribe el archivo).
- `'a'` → Agregar contenido al final del archivo.
- `'r+'` → Lectura y escritura.
- `'wb'`, `'rb'`, `'ab'` → Modos binarios.

Ejemplo de lectura:

```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

```

Ejemplo de escritura:

```python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!")

```

Hay que tener en cuenta que si utilizamos el método de `write_text()` podemos reemplazar todo el texto por lo deseado.

```python
archivo.write_text("\n".join(texto),"utf-8")
# Agrega un salto de línea y luego agrega el texto que hemos cargado en la variable texto

archivo.write_text("hola mundo", "utf-8")
# Piso todo el archivo con el nuevo texto de Hola mundo
```

Siempre es recomendable trabajar con bases de datos en vez de archivos cuando estos son demasiado grandes

### Archivos CSV

Son archivos de valores separados por comas, útiles para almacenar datos tabulares. Python ofrece el módulo `csv` para trabajar con ellos.

Ejemplo de lectura:

```python
import csv

with open("datos.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

```

Ejemplo de escritura:

```python
with open("datos.csv", "w", newline='', encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])
    escritor.writerow(["Ana", 25])

```

### Archivos JSON

Son archivos de texto que almacenan datos en formato JSON (JavaScript Object Notation). Python usa el módulo `json` para manipularlos.

Estoy archivos se utilizan para extraer información de una API o de alguna bbdd no relacional.

Ejemplo de lectura:

```python
import json

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
    print(datos)

```

Ejemplo de escritura:

```python
datos = {"nombre": "Carlos", "edad": 30}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

```

### Archivos Comprimidos

Python maneja archivos comprimidos con los módulos `zipfile` y `tarfile`.

Ejemplo de crear un ZIP:

```python
import zipfile

with zipfile.ZipFile("archivo.zip", "w") as zipf:
    zipf.write("archivo.txt")

```

Ejemplo de extraer un ZIP:

```python
with zipfile.ZipFile("archivo.zip", "r") as zipf:
    zipf.extractall("carpeta_destino")

```