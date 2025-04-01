# Indices de paquetes de Python (Pypi)

# ¿Qué es PyPI?

El **Python Package Index (PyPI)** es el repositorio oficial de paquetes de Python. Es una plataforma donde los desarrolladores pueden publicar y compartir sus librerías para que otros puedan instalarlas fácilmente mediante herramientas como `pip`.

### **Características y ventajas de PyPI:**

- Acceso a miles de bibliotecas listas para usar.
- Instalación sencilla de paquetes y sus dependencias.
- Actualización de paquetes de manera eficiente.
- Facilita la distribución y publicación de proyectos propios.

---

# `pip`: Instalador de Paquetes de Python

`pip` es la herramienta oficial para instalar paquetes desde PyPI.

### **(En Windows) Comandos básicos de `pip`:**

(En Linux): `pip3` :

- **Instalar un paquete:**
    
    ```
    pip install nombre_del_paquete
    
    ```
    
- **Instalar una versión específica:**
    
    ```
    pip install nombre_del_paquete==1.2.3
    
    ```
    
- **Actualizar un paquete:**
    
    ```
    pip install --upgrade nombre_del_paquete
    
    ```
    
- **Listar paquetes instalados:**
    
    ```
    pip list
    
    ```
    
- **Desinstalar un paquete:**
    
    ```
    pip uninstall nombre_del_paquete
    
    ```
    

---

# Ambientes Virtuales

Un **ambiente virtual** en Python es un entorno aislado donde puedes instalar paquetes sin afectar el sistema global.

### **Creación y uso de ambientes virtuales con `venv`:**

1. **Crear un ambiente virtual:**
    
    ```
    python -m venv mi_entorno
    
    ```
    
2. **Activar el ambiente virtual:**
    - En Windows:
        
        ```
        mi_entorno\Scripts\activate
        
        ```
        
    - En Linux/Mac:
        
        ```
        source mi_entorno/bin/activate
        
        ```
        
3. **Desactivar el ambiente virtual:**
    
    ```
    deactivate
    
    ```
    

### **Ventajas de los ambientes virtuales:**

- Evitan conflictos entre dependencias de distintos proyectos.
- Permiten probar versiones específicas de paquetes.
- Facilitan la portabilidad del proyecto.

---

# Versionado de paquetes

Los números de versión en los paquetes de `pip` siguen el esquema **SemVer** (**Versionado Semántico**), que se estructura como:

```
MAJOR.MINOR.PATCH
```

Si tomamos el ejemplo **2.28.1**, se interpreta así:

- **2** → **(MAJOR)** Versión mayor: cambios incompatibles con versiones anteriores.
- **28** → **(MINOR)** Versión menor: agrega nuevas funcionalidades sin romper compatibilidad.
- **1** → **(PATCH)** Parche: correcciones de errores o mejoras menores sin agregar nuevas funciones.

🔹 **Ejemplo práctico con `requests 2.28.1`**

- **Si cambia de 2.28.1 → 3.0.0** → Hay cambios grandes que podrían romper compatibilidad.
- **Si cambia de 2.28.1 → 2.29.0** → Se agregaron funciones nuevas, pero sigue siendo compatible con 2.28.x.
- **Si cambia de 2.28.1 → 2.28.2** → Solo arreglos menores sin afectar el funcionamiento.

### 📌 Extras:

- A veces hay versiones **beta, alpha o release candidates**, como:
    - `1.0.0-alpha` → Versión en fase temprana.
    - `1.0.0-rc1` → Casi lista para producción (release candidate).
- También puedes usar versiones específicas en `pip`:
    
    ```bash
    pip install requests==2.28.1  # Instala exactamente la versión 2.28.1
    pip install requests>=2.28.0  # Instala la última versión igual o superior a 2.28.0
    
    ```
    

---

# Paquetes instalados por defecto

### 🔹 **Paquetes relacionados con Python y el formateo de código**

1. **`autopep8` (2.3.2)** → Formatea código Python automáticamente según la guía de estilo **PEP 8**.
    - 📌 Sirve para corregir espacios, indentación, saltos de línea, etc.
    - ⚡ Uso: `autopep8 --in-place archivo.py` (aplica el formateo).
2. **`pycodestyle` (2.12.1)** → Verifica que el código cumpla con **PEP 8**, pero sin modificarlo.
    - 📌 Se usa para revisar si el código tiene errores de estilo.
    - ⚡ Uso: `pycodestyle archivo.py`.

### 🔹 **Paquetes relacionados con redes y seguridad**

1. **`certifi` (2025.1.31)** → Proporciona certificados SSL/TLS para conexiones seguras.
    - 📌 Lo usa `requests`, `urllib3`, y otros para verificar la seguridad de las conexiones HTTPS.
2. **`charset-normalizer` (3.4.1)** → Detecta y maneja diferentes codificaciones de texto.
    - 📌 Se usa en peticiones HTTP para interpretar correctamente caracteres especiales.
3. **`idna` (3.10)** → Maneja dominios en **Internationalized Domain Names (IDN)**.
    - 📌 Permite trabajar con URLs que contienen caracteres no ASCII (ejemplo: `español.com`).
4. **`urllib3` (2.3.0)** → Biblioteca para realizar peticiones HTTP avanzadas.
    - 📌 Lo usan paquetes como `requests` para gestionar conexiones a internet de forma segura y eficiente.

### 🔹 **Paquetes relacionados con la gestión de Python y sus dependencias**

1. **`pip` (25.0.1)** → Gestor de paquetes de Python.
    - 📌 Permite instalar, actualizar y desinstalar paquetes de PyPI.
    - ⚡ Uso: `pip install paquete`, `pip list`, `pip uninstall paquete`.
2. **`wheel` (0.45.1)** → Formato de distribución de paquetes Python.
    - 📌 Hace que la instalación de paquetes sea más rápida.
    - ⚡ Se usa cuando creas y subes paquetes a PyPI (`python setup.py bdist_wheel`).

---

### **📌 Conclusión**

- **Si programas en Python**, `autopep8` y `pycodestyle` te ayudan con el estilo del código.
- **Si trabajas con APIs o peticiones web**, `urllib3`, `certifi`, `charset-normalizer`, e `idna` son clave.
- **Si manejas paquetes en Python**, `pip` y `wheel` optimizan la instalación y distribución.

---

# `pipenv`: Alternativa a `venv` y `pip`

`pipenv` es una herramienta que gestiona ambientes virtuales y dependencias de manera más organizada.

### **Características de `pipenv`:**

- Combina `pip` y `venv` en una sola herramienta.
- Usa un archivo `Pipfile` en lugar de `requirements.txt`.
- Permite asegurar versiones de dependencias con `Pipfile.lock`.

### **Comandos básicos de `pipenv`:**

- **Crear un ambiente virtual e instalar un paquete:**
    
    ```
    pipenv install nombre_del_paquete
    
    ```
    
- **Activar el ambiente virtual:**
    
    ```
    pipenv shell
    
    ```
    
- **Desinstalar un paquete:**
    
    ```
    pipenv uninstall nombre_del_paquete
    
    ```
    
- **Listar dependencias:**
    
    ```
    pipenv graph
    
    ```
    

---

# Gestión de Dependencias

La gestión de dependencias se refiere a la administración de bibliotecas externas en un proyecto.

### **Opciones para gestionar dependencias:**

1. **`requirements.txt` (método tradicional con `pip`)**
    - Crear un archivo con:
        
        ```
        pip freeze > requirements.txt
        
        ```
        
    - Instalar dependencias desde un archivo:
        
        ```
        pip install -r requirements.txt
        
        ```
        
2. **`Pipfile` y `Pipfile.lock` (usando `pipenv`)**
    - `Pipfile` describe las dependencias del proyecto.
    - `Pipfile.lock` asegura versiones exactas para replicabilidad.

### **Recomendaciones:**

- Usar `requirements.txt` si trabajas con `pip`.
- Usar `Pipfile` si prefieres `pipenv` para mayor organización.
- Mantener las dependencias actualizadas y bien documentadas.

---

# Creación y Publicación de un Paquete Python en PyPI

## 1. Estructura básica de un paquete Python

Primero, creemos la estructura de directorios para tu paquete:

```
mi_paquete/
├── mi_paquete/                # Directorio principal del paquete
│   ├── __init__.py            # Archivo que hace que Python trate el directorio como un paquete
│   ├── modulo_principal.py    # Tu código principal
│   └── herramientas.py        # Módulo adicional (opcional)
├── tests/                     # Directorio para pruebas
│   ├── __init__.py
│   └── test_modulo.py
├── docs/                      # Documentación
├── README.md                  # Descripción del proyecto
├── LICENSE                    # Licencia del software
├── pyproject.toml             # Configuración de construcción del paquete
└── setup.cfg                  # Configuración adicional (opcional)

```

## 2. Creando los archivos principales

### `mi_paquete/__init__.py`

```python
"""Paquete de ejemplo para demostrar creación y publicación de paquetes Python.

Este paquete proporciona funcionalidades básicas para demostrar
cómo estructurar, documentar y publicar un paquete Python.
"""

__version__ = "0.1.0"
__author__ = "Tu Nombre <tu@email.com>"
__all__ = []  # Lista de módulos que se importarán con "from mi_paquete import *"

```

### `mi_paquete/modulo_principal.py`

```python
"""Módulo principal del paquete que contiene funcionalidades clave."""

def saludar(nombre: str) -> str:
    """Genera un saludo personalizado.

    Args:
        nombre (str): Nombre de la persona a saludar.

    Returns:
        str: Mensaje de saludo.

    Examples:
        >>> saludar("Juan")
        '¡Hola, Juan! Bienvenido al paquete.'
    """
    return f"¡Hola, {nombre}! Bienvenido al paquete."

def suma(a: float, b: float) -> float:
    """Suma dos números y devuelve el resultado.

    Args:
        a (float): Primer número a sumar.
        b (float): Segundo número a sumar.

    Returns:
        float: Resultado de la suma.

    Raises:
        TypeError: Si alguno de los argumentos no es numérico.

    Examples:
        >>> suma(2, 3)
        5.0
        >>> suma(1.5, 2.5)
        4.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser numéricos")
    return float(a + b)

```

## 3. Documentación profesional

### `README.md`

```markdown
# mi_paquete

[![PyPI version](<https://badge.fury.io/py/mi-paquete.svg>)](<https://pypi.org/project/mi-paquete/>)
[![License: MIT](<https://img.shields.io/badge/License-MIT-yellow.svg>)](<https://opensource.org/licenses/MIT>)

Un paquete Python de ejemplo que demuestra cómo crear, documentar y publicar un paquete en PyPI.

## Instalación

```bash
pip install mi-paquete

```

## Uso

```python
from mi_paquete import modulo_principal

# Saludar a un usuario
print(modulo_principal.saludar("Ana"))

# Sumar dos números
resultado = modulo_principal.suma(5, 3.5)
print(f"El resultado es: {resultado}")

```

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT - ver [LICENSE](https://www.notion.so/LICENSE) para más detalles.

```

### Documentación con Sphinx (opcional pero recomendado)

Instala Sphinx:
```bash
pip install sphinx sphinx-rtd-theme

```

Crea la documentación:

```bash
cd docs
sphinx-quickstart

```

Configura `docs/conf.py`:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

# Theme
html_theme = 'sphinx_rtd_theme'

```

Genera la documentación:

```bash
sphinx-apidoc -o . ../mi_paquete
make html

```

## 4. Configuración para PyPI

### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

```

### `setup.cfg`

```
[metadata]
name = mi-paquete
version = 0.1.0
author = Tu Nombre
author_email = tu@email.com
description = Un paquete Python de ejemplo
long_description = file: README.md
long_description_content_type = text/markdown
url = <https://github.com/tuusuario/mi_paquete>
project_urls =
    Bug Tracker = <https://github.com/tuusuario/mi_paquete/issues>
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = .
packages = find:
python_requires = >=3.6
install_requires =

[options.packages.find]
where = .

```

## 5. Publicación en PyPI

### 1. Crea las distribuciones

```bash
pip install build
python -m build

```

### 2. Instala twine (para subir el paquete)

```bash
pip install twine

```

### 3. Sube a TestPyPI (para pruebas)

```bash
twine upload --repository testpypi dist/*

```

### 4. Instala desde TestPyPI para probar

```bash
pip install --index-url <https://test.pypi.org/simple/> --no-deps mi-paquete

```

### 5. Cuando todo esté bien, sube a PyPI real

```bash
twine upload dist/*

```

## 6. Buenas prácticas adicionales

1. **Control de versiones**: Usa semantic versioning (MAJOR.MINOR.PATCH)
2. **Pruebas**: Añade pruebas en el directorio `tests/`
3. **GitHub Actions**: Configura CI/CD para pruebas automáticas
4. [**CHANGELOG.md**](http://changelog.md/): Mantén un registro de cambios
5. **Type hints**: Como ves en el ejemplo, añade tipado para mejor documentación

## Ejemplo de `.gitignore`

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Documentation
docs/_build/

```

---

# Cómo Documentar un Paquete en Python

Para documentar un paquete en Python de manera efectiva, se recomienda:

1. **Escribir un `README.md`** con:
    - Descripción del paquete.
    - Cómo instalarlo.
    - Ejemplos de uso.
    - Contacto o contribuciones.
2. **Agregar `docstrings` a las funciones y clases:**
    
    ```python
    def sumar(a: int, b: int) -> int:
        """Retorna la suma de dos números."""
        return a + b
    
    ```
    
3. **Usar herramientas como `Sphinx` para documentación avanzada.**
    
    ```
    pip install sphinx
    sphinx-quickstart
    
    ```
    

---

# Cómo Publicar un Paquete en PyPI

Si deseas compartir tu paquete en PyPI, sigue estos pasos:

### **1. Crear los archivos necesarios**

En la raíz del proyecto, asegúrate de tener:

- **`setup.py`** (Define la metadata del paquete)
- **`README.md`** (Descripción del paquete)
- **Código fuente** dentro de una carpeta (ej. `mi_paquete/`)

Ejemplo de `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="mi_paquete",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],  # Dependencias
    author="Tu Nombre",
    description="Descripción breve del paquete",
    url="https://github.com/tu_usuario/mi_paquete",
)

```

### **2. Construir el paquete**

```
python setup.py sdist bdist_wheel

```

### **3. Subirlo a PyPI**

```
pip install twine
twine upload dist/*

```

### **4. Instalarlo desde PyPI**

```
pip install mi_paquete
```

---