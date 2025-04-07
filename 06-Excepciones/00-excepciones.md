# Excepciones

Las excepciones en Python son eventos que ocurren durante la ejecución de un programa que interrumpen el flujo normal de las instrucciones. Cuando ocurre un error durante la ejecución, Python genera (o "lanza") una excepción.

### Características principales

- Son objetos que representan errores
- Permiten manejar errores de forma controlada
- Pueden ser capturadas y manejadas usando bloques try/except
- Python tiene excepciones predefinidas y permite crear excepciones personalizadas

### Estructura básica del manejo de excepciones

```python
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre la excepción
    print("Error: División por cero")
finally:
    # Código que se ejecuta siempre
    print("Proceso terminado")
```

### Excepciones comunes en Python

- **`ZeroDivisionError`:** División por cero
- **`TypeError`:** Operación con tipos de datos incompatibles
- **`ValueError`:** Operación con valor inapropiado
- **`NameError`:** Variable o nombre no definido
- **`IndexError`:** Índice fuera de rango
- **`FileNotFoundError`:** Archivo no encontrado

### Beneficios del manejo de excepciones

- Mejora la robustez del programa
- Permite manejar errores de forma elegante
- Facilita la depuración del código
- Ayuda a crear programas más confiables

---

# Tipos de excepciones

### 1. Excepciones incorporadas (Built-in Exceptions)

Son las excepciones predefinidas que vienen con Python. Incluyen errores comunes como `TypeError`, `ValueError`, etc.

### 2. Excepciones del usuario (User-Defined Exceptions)

Son excepciones personalizadas creadas por el programador heredando de la clase `Exception`.

```python
class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
```

### 3. Excepciones de sintaxis (Syntax Exceptions)

Errores que ocurren cuando el código viola las reglas sintácticas de Python (`SyntaxError`).

### 4. Excepciones lógicas (Logical Exceptions)

Errores que ocurren durante la ejecución debido a problemas lógicos en el código (`RuntimeError`).

### 5. Excepciones del sistema (System Exceptions)

Errores relacionados con el sistema operativo o el entorno de ejecución (`OSError`, `IOError`).

Todas estas excepciones forman parte de una jerarquía, donde `BaseException` es la clase base de la que heredan todas las demás excepciones.

---

## Bloques else, finally

Los bloques `else` y `finally` son componentes adicionales en el manejo de excepciones:

### Bloque else

El bloque `else` se ejecuta cuando no ocurre ninguna excepción en el bloque `try`. Es útil para código que debe ejecutarse si la operación fue exitosa.

```python
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("No es un número válido")
else:
    print(f"El número ingresado es: {numero}")  # Se ejecuta si no hay error
```

### Bloque finally

El bloque `finally` se ejecuta siempre, independientemente de si ocurrió una excepción o no. Es útil para tareas de limpieza como cerrar archivos o conexiones.

```python
try:
    archivo = open("datos.txt", "r")
    # Procesar archivo
except FileNotFoundError:
    print("El archivo no existe")
finally:
    archivo.close()  # Se ejecuta siempre, haya error o no
```

La estructura completa del manejo de excepciones puede ser:

```python
try:
    # Código que puede generar excepción
except:
    # Manejo de la excepción
else:
    # Se ejecuta si no hay excepción
finally:
    # Se ejecuta siempre
```