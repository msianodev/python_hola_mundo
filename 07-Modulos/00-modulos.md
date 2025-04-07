# Módulos

Los módulos en Python son archivos que contienen definiciones y declaraciones de Python, como funciones, clases y variables. Permiten organizar y reutilizar el código de manera eficiente. Un módulo es simplemente un archivo `.py`, y su nombre será el nombre del archivo sin la extensión `.py`.

Para utilizarlos de manera correcta y como una buena práctica, es importante seguir estas recomendaciones:

- **Modularidad**: Divide el código en módulos que tengan funcionalidades específicas.
- **Nombres Significativos**: Usa nombres descriptivos para los módulos que indiquen claramente su propósito.
- **Encapsulamiento**: Mantén las variables y funciones internas de un módulo protegidas para evitar conflictos de nombres.
- **Documentación**: Documenta cada módulo, explicando qué hace y cómo se debe usar.

## Módulos Compilados

Un módulo compilado es un archivo de bytecode (pycode) generado a partir de un archivo fuente de Python `.py`. Estos archivos tienen la extensión `.pyc` y se generan automáticamente para mejorar el rendimiento en posteriores ejecuciones. Un archivo compilado evita la necesidad de compilar el código fuente cada vez que se ejecuta, acelerando así el tiempo de carga del módulo.

## Paquetes

Un paquete es una colección de módulos organizados en directorios. Contiene un archivo especial `__init__.py` que indica a Python que el directorio debe ser tratado como un paquete. Los paquetes permiten una estructura jerárquica para módulos, facilitando la organización y reutilización del código.

```markdown
# Estructura de un paquete
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py

```

Los módulos apuntan a archivos.

Los paquetes apuntan a carpetas.

Supongamos el caso que tenemos un paquete llamado `usuarios` donde adentro vamos a tener un módulo de python llamado `acciones.py` . Dicho módulo va a contener la función de `guardar()` y de `pagar_impuestos()` . En nuestro archivo de aplicación vamos a importar lo siguiente:

```python
# Formas de importar módulos:

# Forma ideal N°1:
from usuarios.acciones import guardar
# Lo que hacemos es importar el paquete de usuarios, punto y vscode nos sugiere
# importar el módulo correspondiente que es acciones.
# Luego con import guardar importamos sólo la funcion de guardar()
# El llamado a la funcion sería de la siguiente manera:
guardar() # Output: "Guardando"

# Forma ideal N°2:
# Otra manera mas óptima de importar las funciones de un módulo que se encuentra
# dentro de un paquete:
from usuarios import acciones
# De esta manera importamos las funciones específicas dentro de ese módulo
acciones.guardar() # Output: "Guardando"

# Otra forma de importar es la siguiente (bastante tediosa, no convencional):
import usuarios.acciones
# De esta forma hacemos referencia a todas las funciones dentro de acciones
# pero en el llamado de cada una de esas funciones nos quedaría de la siguiente manera:
usuarios.acciones.guardar() # Output: "Guardando"

```

## Subpaquetes

Los subpaquetes son paquetes dentro de otros paquetes. Permiten una organización aún más detallada del código. Cada subpaquete también contiene su propio archivo `__init__.py`.

```markdown
# Estructura de un paquete con subpaquetes
mi_paquete/
    __init__.py
    subpaquete1/
        __init__.py
        modulo1.py
    subpaquete2/
        __init__.py
        modulo2.py

```

## Referenciando Sub Paquetes

Para referenciar subpaquetes y módulos dentro de ellos, se utiliza la notación de punto. Por ejemplo, si tienes un módulo `modulo1` dentro del subpaquete `subpaquete1`, lo puedes importar así:

```python
from mi_paquete.subpaquete1 import modulo1

```

Supongamos que tenemos la siguiente jerarquía de paquetes y modulos:

```markdown
usuarios/
    __init__.py
    gestion/
        __init__.py
        crud.py
    subpaquete2/
        __init__.py
        modulo2.py
```

El referenciado en el importador quedaría de la siguiente manera:

```python
from usuarios.gestion.crud import guardar
# Referenciando desde la jerarquía más alta o al mismo nivel del módulo de donde
# lo llamamos, podemos acceder.
guardar() # Output: Guardando...

# Si quisiera navegar en otros paquetes para traerme otra funcion de otro módulo
# se puede hacer de esta manera:
from ..utilidades.impuestos import pagar_impuestos
# De esta manera lo que logramos es navegar en los directorios hacia atras para
# salir del paquete actual y yendo a buscar el otro paquete para importar otra
# funcion de otro módulo
pagar_impuestos() # Output: Pagando impuestos..
```

## Dir

La función `dir()` es útil para listar todos los nombres definidos en un módulo. Esto incluye funciones, variables y clases. Es útil para explorar el contenido de un módulo y depurar.

```python
import mi_paquete.subpaquete1.modulo1
print(dir(mi_paquete.subpaquete1.modulo1))

```

En Python, la función `dir()` devuelve una lista de los atributos y métodos de un objeto. Si la aplicas sobre una clase o un objeto, verás métodos especiales (también llamados **métodos mágicos**) que comienzan y terminan con doble guion bajo (`__`).

Estos métodos mágicos permiten personalizar el comportamiento de las clases en Python, como la inicialización, la representación en texto, las operaciones aritméticas y más. Aquí tienes algunos de los más comunes:

### 🔹 Métodos de Inicialización y Representación

- `__init__(self, ...)` → Se ejecuta al instanciar un objeto (constructor).
- `__str__(self)` → Define la representación en texto del objeto para `print()`.
- `__repr__(self)` → Representación oficial del objeto (para depuración y desarrollo).
- `__del__(self)` → Se llama cuando un objeto es destruido.

### 🔹 Métodos de Comparación

- `__eq__(self, other)` → Define `==` (igualdad).
- `__ne__(self, other)` → Define `!=` (desigualdad).
- `__lt__(self, other)` → Define `<` (menor que).
- `__le__(self, other)` → Define `<=` (menor o igual que).
- `__gt__(self, other)` → Define `>` (mayor que).
- `__ge__(self, other)` → Define `>=` (mayor o igual que).

### 🔹 Métodos Aritméticos

- `__add__(self, other)` → Define `+` (suma).
- `__sub__(self, other)` → Define `` (resta).
- `__mul__(self, other)` → Define `` (multiplicación).
- `__truediv__(self, other)` → Define `/` (división).
- `__floordiv__(self, other)` → Define `//` (división entera).
- `__mod__(self, other)` → Define `%` (módulo).
- `__pow__(self, other)` → Define `*` (potenciación).

### 🔹 Métodos de Contenedores (Listas, Diccionarios, etc.)

- `__len__(self)` → Devuelve la cantidad de elementos (`len(obj)`).
- `__getitem__(self, key)` → Permite acceder con `obj[key]`.
- `__setitem__(self, key, value)` → Permite asignar con `obj[key] = value`.
- `__delitem__(self, key)` → Elimina elementos con `del obj[key]`.
- `__contains__(self, item)` → Se usa en `in`, por ejemplo: `item in obj`.

### 🔹 Métodos de Iteración

- `__iter__(self)` → Devuelve un iterador (`for item in obj`).
- `__next__(self)` → Define el siguiente elemento en una iteración.

### 🔹 Métodos de Llamado

- `__call__(self, *args, **kwargs)` → Hace que el objeto sea invocable (`obj()`).

### 🔹 Métodos de Contexto (`with`)

- `__enter__(self)` → Se ejecuta al entrar en un bloque `with`.
- `__exit__(self, exc_type, exc_value, traceback)` → Se ejecuta al salir del `with`.

Puedes ver todos los métodos especiales disponibles en Python ejecutando:

```python
print(dir(object))

```

¿Necesitas ayuda con algún método en particular? 🚀

## Paquetes con Nombres Dinámicos

Puedes importar paquetes usando nombres dinámicos utilizando la función `importlib.import_module()`. Esto es útil cuando el nombre del módulo se determina en tiempo de ejecución.

```python
import importlib

nombre_del_modulo = 'mi_paquete.subpaquete1.modulo1'
modulo = importlib.import_module(nombre_del_modulo)

```

## Import Condicionados

Los import condicionados se utilizan cuando necesitas importar un módulo solo bajo ciertas condiciones. Esto puede ser útil para evitar dependencias circulares o cargar módulos costosos solo cuando son necesarios.

```python
if alguna_condicion:
    import modulo_costoso
    modulo_costoso.algun_metodo()

```