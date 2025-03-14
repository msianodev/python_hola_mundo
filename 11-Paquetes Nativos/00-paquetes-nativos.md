# Paquetes nativos de Python

Python incluye una gran cantidad de **paquetes nativos** (módulos estándar) que permiten manejar diversas funcionalidades sin necesidad de instalar librerías externas. Aquí tienes un resumen de los módulos más relevantes para lo que necesitas:

---

### 🌐 **Manejo de Browser (Web)**

**Módulo relevante:** `webbrowser`

🔹 **Funcionalidad:** Abre URLs en el navegador predeterminado del usuario.

**Ejemplo de uso:**

```python
import webbrowser
webbrowser.open("https://www.python.org")  # Abre la URL en el navegador

```

---

### 📅 **Fechas y Tiempos**

**Módulo relevante:** `datetime`

🔹 **Funcionalidad:** Manejo de fechas, horas y operaciones con tiempo.

**Ejemplo de uso:**

```python
from datetime import datetime
ahora = datetime.now()
print(ahora.strftime("%Y-%m-%d %H:%M:%S"))  # Formatear fecha y hora

```

---

### ⏳ **Tiempo y Diferencias de Tiempo**

**Módulo relevante:** `datetime.timedelta`

🔹 **Funcionalidad:** Representa diferencias de tiempo para sumas/restas.

**Ejemplo de uso:**

```python
from datetime import datetime, timedelta
hoy = datetime.now()
mañana = hoy + timedelta(days=1)
print(mañana)  # Fecha de mañana

```

---

### 🎲 **Generación de Números Aleatorios**

**Módulo relevante:** `random`

🔹 **Funcionalidad:** Generación de números aleatorios y selección aleatoria de elementos.

**Ejemplo de uso:**

```python
import random
print(random.randint(1, 100))  # Número aleatorio entre 1 y 100
print(random.choice(["rojo", "verde", "azul"]))  # Elección aleatoria

```

---

### 🖥️ **Argumentos en la Línea de Comandos**

**Módulo relevante:** `argparse`

🔹 **Funcionalidad:** Manejo de argumentos en scripts ejecutados desde la CLI.

**Ejemplo de uso:**

```python
import argparse

parser = argparse.ArgumentParser(description="Ejemplo de CLI")
parser.add_argument("--nombre", type=str, help="Tu nombre")
args = parser.parse_args()

print(f"Hola, {args.nombre}!")  # Ejecutar con: python script.py --nombre "Juan"

```

---

### 📧 **Enviar Correos Electrónicos**

**Módulo relevante:** `smtplib`

🔹 **Funcionalidad:** Envío de correos mediante SMTP.

Simple Mail Transfer Protocol: Este protocolo es utilizado por muchos servicios actualmente, es usado por Gmail. Hay algunos que tienen su propia forma. Esto solamente funciona para SMTP.

**Ejemplo de uso:**

```python
import smtplib

servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls()
servidor.login("tu_correo@gmail.com", "tu_contraseña")
servidor.sendmail("tu_correo@gmail.com", "destino@gmail.com", "Asunto: Hola\n\nEste es un mensaje.")
servidor.quit()

```

⚠️ **Nota:** Para Gmail, es posible que necesites activar "Acceso de apps menos seguras" o usar una **App Password**.

---

### 📝 **Manejo de Plantillas de Texto**

**Módulo relevante:** `string.Template`

🔹 **Funcionalidad:** Permite crear plantillas con variables reemplazables.

**Ejemplo de uso:**

```python
from string import Template

plantilla = Template("Hola, $nombre. Bienvenido a $lugar.")
mensaje = plantilla.substitute(nombre="Juan", lugar="PythonLandia")
print(mensaje)

```

💡 Para plantillas más avanzadas, usa **Jinja2** (requiere instalación externa).

---