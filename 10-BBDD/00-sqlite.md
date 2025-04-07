# SQLite

Para comenzar a trabajar con **SQLite** en **Python**, puedes seguir estos pasos:

---

### 1️⃣ **Importar la librería**

Python incluye `sqlite3` en la biblioteca estándar, así que no necesitas instalar nada extra.

```python
import sqlite3

```

---

### 2️⃣ **Conectarse a la base de datos**

SQLite usa archivos `.db` para almacenar los datos. Si el archivo no existe, se creará automáticamente.

```python
conn = sqlite3.connect("mi_base_de_datos.db")
cursor = conn.cursor()  # Obtenemos el cursor para ejecutar consultas

```

Con `conn` creamos y gestionamos la conexión a la base de datos. Con `cursor` creamos las consultas

También puedes usar `:memory:` si quieres una base de datos en RAM, sin archivo físico:

```python
conn = sqlite3.connect(":memory:")

```

---

### 3️⃣ **Crear una tabla**

Ejemplo de una tabla para almacenar usuarios:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
""")
conn.commit()  # Guardamos los cambios

```

---

### 4️⃣ **Insertar datos**

Puedes insertar datos con `execute` o `executemany`:

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 25))
conn.commit()  # Guardamos los cambios

```

Para insertar varios datos a la vez:

```python
usuarios = [("Ana", 30), ("Pedro", 40), ("Maria", 22)]
cursor.executemany("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", usuarios)
conn.commit()

```

---

### 5️⃣ **Consultar datos**

```python
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

```

Si necesitas solo un registro:

```python
cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", ("Ana",))
usuario = cursor.fetchone()
print(usuario)  # Resultado: (id, "Ana", 30)

```

---

### 6️⃣ **Actualizar datos**

```python
cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (35, "Ana"))
conn.commit()

```

---

### 7️⃣ **Eliminar datos**

```python
cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Pedro",))
conn.commit()

```

---

### 8️⃣ **Cerrar la conexión**

Siempre es importante cerrar la conexión cuando termines.

```python
conn.close()

```

---

### 📝 **Consejos adicionales**

- Usa **"with"** para manejar la conexión de forma segura:
    
    ```python
    with sqlite3.connect("mi_base_de_datos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        print(cursor.fetchall())
    
    ```
    
    Esto asegura que la conexión se cierre automáticamente.
    
- Activa **"modo diccionario"** para trabajar con nombres de columnas en lugar de índices:
    
    ```python
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuario = cursor.fetchone()
    print(dict(usuario))  # {'id': 1, 'nombre': 'Juan', 'edad': 25}
    
    ```
    

---

### 🚨 **SQL Injection y cómo evitarlo en SQLite con Python**

**SQL Injection** es una técnica en la que un atacante manipula una consulta SQL al ingresar valores maliciosos, lo que puede comprometer la base de datos. Esto sucede cuando las consultas son construidas con concatenación de strings en lugar de usar consultas parametrizadas.

---

## 1️⃣ **Ejemplo de SQL Injection (MAL)**

Si construyes la consulta con concatenación de strings, un atacante puede modificarla.

```python
import sqlite3

conn = sqlite3.connect("mi_base_de_datos.db")
cursor = conn.cursor()

usuario = "Juan"
edad = "25 OR 1=1"  # 🚨 Ataque SQL Injection

query = f"INSERT INTO usuarios (nombre, edad) VALUES ('{usuario}', {edad})"
cursor.execute(query)  # Esto ejecutará un INSERT con una condición siempre verdadera

conn.commit()
conn.close()

```

🔴 **Riesgo:** Un atacante podría insertar valores sin restricción o ejecutar otras consultas maliciosas.

---

## 2️⃣ **Cómo evitarlo con `execute()` (BIEN ✅)**

Siempre usa **consultas parametrizadas con `?`** en lugar de concatenar valores en la consulta.

```python
usuario = "Juan"
edad = 25

cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (usuario, edad))
conn.commit()

```

**¿Por qué funciona?**

- `sqlite3` escapa automáticamente los valores, evitando que se interpreten como código SQL.
- No importa si el usuario ingresa `"25 OR 1=1"`, será tratado como un string en lugar de código SQL.

---

## 3️⃣ **Ejemplo con `executemany()` para insertar múltiples datos de forma segura**

Si quieres insertar varios usuarios sin riesgo de SQL Injection:

```python
usuarios = [("Ana", 30), ("Pedro", 40), ("Maria", 22)]
cursor.executemany("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", usuarios)
conn.commit()

```

---

## 4️⃣ **Ejemplo de consulta segura (`SELECT`)**

La inyección también puede ocurrir al hacer búsquedas si no usas parámetros correctamente.

🚨 **MAL** (Vulnerable a SQL Injection):

```python
nombre = "Juan' OR '1'='1"  # Un atacante intenta manipular la consulta
query = f"SELECT * FROM usuarios WHERE nombre = '{nombre}'"
cursor.execute(query)  # 🚨 Esto devuelve todos los registros si la inyección funciona

```

✅ **BIEN** (Consulta segura con parámetros):

```python
cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))

```

---

## 🚀 **Resumen de Buenas Prácticas**

1. **Usa siempre `?` en `execute()` y `executemany()` en lugar de concatenación de strings.**
2. **Nunca confíes en los datos de entrada del usuario.**
3. **Usa `conn.row_factory = sqlite3.Row` para trabajar con nombres de columnas en lugar de índices.**
4. **Cierra siempre la conexión con `conn.close()` o usa `with sqlite3.connect(...) as conn:` para manejarla automáticamente.**