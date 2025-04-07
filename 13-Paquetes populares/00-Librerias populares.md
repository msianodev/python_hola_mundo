# Librerías más populares de Python

# **Variables de entorno**

Son valores que el sistema operativo usa para configurar el comportamiento de procesos y aplicaciones. En Python, se pueden leer y modificar usando el módulo `os`. Se utilizan comúnmente para almacenar credenciales, rutas o configuraciones sensibles.

Ejemplo en Python:

```python
import os

# Obtener una variable de entorno
db_user = os.getenv("DB_USER")

# Establecer una variable de entorno
os.environ["API_KEY"] = "123456"

```

---

## **Pipenv**

Es una herramienta para gestionar dependencias de Python de manera más eficiente que `pip` y `virtualenv`. Combina la instalación de paquetes y la gestión de entornos virtuales en un solo comando.

### **Características de Pipenv**

1. **Manejo automático de entornos virtuales**: Crea un entorno virtual dentro del proyecto.
2. **Uso de `Pipfile` y `Pipfile.lock`**: En lugar de `requirements.txt`, usa `Pipfile` para registrar dependencias y `Pipfile.lock` para fijar versiones exactas.
3. **Mayor seguridad**: Pipenv verifica la integridad de las dependencias con `hashes`.
4. **Fácil instalación y desinstalación de paquetes**: Maneja dependencias sin necesidad de activarlas manualmente.

### **Ejemplo de uso**

1. Instalar `pipenv`:
    
    ```
    pip install pipenv
    
    ```
    
2. Crear un entorno y agregar una librería:
    
    ```
    pipenv install requests
    
    ```
    
3. Activar el entorno:
    
    ```
    pipenv shell
    
    ```
    
4. Ver las dependencias:
    
    ```
    pipenv graph
    
    ```
    

---

# **¿Qué es SendGrid?**

SendGrid es un servicio de envío de correos electrónicos en la nube. Permite enviar emails transaccionales y de marketing con una API fácil de usar. Es útil para enviar correos automatizados, notificaciones o confirmaciones desde aplicaciones en Python.

---

## **Configuración de SendGrid en Python usando Pipenv**

1. **Instalar SendGrid con Pipenv**
    
    Primero, instala SendGrid dentro de tu entorno virtual:
    
    ```
    pipenv install sendgrid
    
    ```
    
2. **Crear una cuenta en SendGrid**
    - Ve a [https://sendgrid.com/](https://sendgrid.com/) y crea una cuenta gratuita.
    - Accede a **API Keys** en el dashboard de SendGrid.
    - Genera una nueva clave de API con permisos de envío de correo y guárdala.
3. **Configurar la clave de API como variable de entorno**
    
    En Windows (CMD o PowerShell):
    
    ```
    set SENDGRID_API_KEY="tu_api_key_aquí"
    
    ```
    
    En Linux/Mac (bash/zsh):
    
    ```
    export SENDGRID_API_KEY="tu_api_key_aquí"
    
    ```
    
4. **Enviar un correo con Python**
    
    Crea un archivo Python, por ejemplo `send_email.py`, y usa el siguiente código:
    
    ```python
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    
    # Obtener la API Key desde variables de entorno
    api_key = os.getenv("SENDGRID_API_KEY")
    
    # Crear el mensaje de correo
    message = Mail(
        from_email="tu_correo@tudominio.com",
        to_emails="destinatario@example.com",
        subject="Hola desde SendGrid",
        html_content="<strong>Este es un email de prueba enviado con Python y SendGrid</strong>"
    )
    
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f"Correo enviado, código de respuesta: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar correo: {e}")
    
    ```

    
5. **Ejecutar el script**
    
    ```
    pipenv run python send_email.py
    
    ```
    

---

### **Notas importantes**

- Asegúrate de usar un correo remitente validado en SendGrid.
- Si estás en un plan gratuito, necesitas verificar manualmente los destinatarios antes de enviar correos.
- Para producción, puedes almacenar la API Key en un archivo `.env` y usar `dotenv` para cargarla en tu script.

---

# **¿Qué es Twilio?**

Twilio es una plataforma de comunicación en la nube que permite enviar SMS, realizar llamadas, manejar WhatsApp y más mediante su API.

---

## **Configuración de Twilio en Python usando Pipenv**

1. **Instalar Twilio con Pipenv**
    
    ```
    pipenv install twilio
    
    ```
    
2. **Crear una cuenta en Twilio**
    - Ve a [https://www.twilio.com/](https://www.twilio.com/) y crea una cuenta.
    - En el dashboard, obtén:
        - **Account SID**
        - **Auth Token**
        - **Número de teléfono de Twilio** (si usas el modo de prueba, solo puedes enviar SMS a números verificados).
3. **Configurar las credenciales como variables de entorno**
    
    En Windows:
    
    ```
    set TWILIO_ACCOUNT_SID="tu_account_sid"
    set TWILIO_AUTH_TOKEN="tu_auth_token"
    set TWILIO_PHONE_NUMBER="tu_numero_twilio"
    
    ```
    
    En Linux/Mac:
    
    ```
    export TWILIO_ACCOUNT_SID="tu_account_sid"
    export TWILIO_AUTH_TOKEN="tu_auth_token"
    export TWILIO_PHONE_NUMBER="tu_numero_twilio"
    
    ```
    
4. **Enviar un SMS con Python**
    
    Crea un archivo `send_sms.py` y usa este código:
    
    ```python
    import os
    from twilio.rest import Client
    
    # Obtener las credenciales desde variables de entorno
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
    
    # Crear cliente de Twilio
    client = Client(account_sid, auth_token)
    
    # Enviar el SMS
    message = client.messages.create(
        body="Hola, este es un mensaje de prueba enviado con Twilio y Python",
        from_=twilio_phone,
        to="+1234567890"  # Número destino con código de país
    )
    
    print(f"Mensaje enviado con SID: {message.sid}")
    
    ```
    
5. **Ejecutar el script**
    
    ```
    pipenv run python send_sms.py
    
    ```
    

---

### **Notas importantes**

- Twilio en modo prueba solo permite enviar SMS a números verificados en tu cuenta.
- Para producción, debes comprar un número de Twilio y verificar la cuenta.
- Puedes almacenar las credenciales en un archivo `.env` y usar `dotenv` para mayor seguridad.

---

# **¿Qué es una API?**

Una **API (Application Programming Interface)** es un conjunto de reglas que permite a diferentes aplicaciones comunicarse entre sí.

## **¿Qué significa que una API sea REST?**

REST (**Representational State Transfer**) es un estilo de arquitectura para diseñar APIs. Sus principios incluyen:

- Uso de **métodos HTTP** estándar (GET, POST, PUT, DELETE, etc.).
- Uso de **recursos** identificados por URLs.
- **Stateless** (sin estado): cada petición es independiente.
- Uso de **JSON o XML** como formato de datos.

## **¿Qué son los Status Codes?**

Son códigos de respuesta HTTP que indican el resultado de una petición:

- **200 OK** → Éxito.
- **201 Created** → Recurso creado.
- **400 Bad Request** → Error en la solicitud.
- **401 Unauthorized** → Falta autenticación.
- **404 Not Found** → Recurso no encontrado.
- **500 Internal Server Error** → Error del servidor.

---

### **Ejemplo básico de API REST con Flask**

Vamos a crear una API REST en Python con Flask que maneje un CRUD de "tareas".

1. **Instalar Flask con Pipenv**
    
    ```
    pipenv install flask
    
    ```
    
2. **Código de la API (`app.py`)**
    
    ```python
    from flask import Flask, request, jsonify
    
    app = Flask(__name__)
    
    # Base de datos simulada
    tasks = [
        {"id": 1, "title": "Aprender API REST", "done": False},
        {"id": 2, "title": "Usar Flask", "done": True}
    ]
    
    # Obtener todas las tareas (GET)
    @app.route("/tasks", methods=["GET"])
    def get_tasks():
        return jsonify(tasks), 200
    
    # Obtener una tarea por ID (GET)
    @app.route("/tasks/<int:task_id>", methods=["GET"])
    def get_task(task_id):
        task = next((t for t in tasks if t["id"] == task_id), None)
        return jsonify(task) if task else ("Not Found", 404)
    
    # Crear una nueva tarea (POST)
    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.json
        new_task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
        tasks.append(new_task)
        return jsonify(new_task), 201
    
    # Actualizar una tarea (PUT)
    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        task = next((t for t in tasks if t["id"] == task_id), None)
        if not task:
            return "Not Found", 404
        data = request.json
        task.update(data)
        return jsonify(task)
    
    # Eliminar una tarea (DELETE)
    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        global tasks
        tasks = [t for t in tasks if t["id"] != task_id]
        return "Deleted", 204
    
    if __name__ == "__main__":
        app.run(debug=True)
    
    ```
    
3. **Ejecutar la API**
    
    ```
    pipenv run python app.py
    
    ```
    
4. **Probar los endpoints con `curl` o Postman**
    - **GET todas las tareas**
        
        ```
        curl -X GET http://127.0.0.1:5000/tasks
        
        ```
        
    - **POST nueva tarea**
        
        ```
        curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "Nueva tarea"}'
        
        ```
        
    - **PUT actualizar tarea**
        
        ```
        curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d '{"done": true}'
        
        ```
        
    - **DELETE una tarea**
        
        ```
        curl -X DELETE http://127.0.0.1:5000/tasks/1
        
        ```
        

---

# **¿Qué son los headers en las solicitudes HTTP?**

Los **headers (encabezados)** en HTTP son metadatos que se envían junto con una solicitud o respuesta. Estos proporcionan información adicional sobre la petición, como el tipo de contenido, autenticación, caché, entre otros.

---

## **¿Para qué sirven los headers?**

Se usan para:

- **Autenticación**: Enviar API Keys, tokens de acceso, etc.
- **Control de contenido**: Indicar el formato de los datos (`JSON`, `XML`).
- **Compresión**: Especificar si se acepta contenido comprimido (`gzip`).
- **Control de caché**: Definir reglas de almacenamiento de la respuesta.

---

### **Ejemplo: Uso de API Key en los headers**

Supongamos que tenemos una API que requiere una **clave de API (API Key)** para autenticarse.

1. **Ejemplo de solicitud con `requests` en Python:**
    
    ```python
    import requests
    
    url = "https://api.ejemplo.com/data"
    headers = {
        "Authorization": "Bearer TU_API_KEY_AQUI",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(response.json())  # Imprime la respuesta en JSON
    else:
        print(f"Error: {response.status_code}")
    
    ```
    
2. **Ejemplo de la API en Flask que valida una API Key:**
    
    ```python
    from flask import Flask, request, jsonify
    
    app = Flask(__name__)
    
    API_KEY = "mi_clave_secreta"
    
    @app.route("/data", methods=["GET"])
    def get_data():
        auth_header = request.headers.get("Authorization")
    
        if not auth_header or auth_header != f"Bearer {API_KEY}":
            return jsonify({"error": "Unauthorized"}), 401
    
        return jsonify({"message": "Acceso permitido", "data": [1, 2, 3]}), 200
    
    if __name__ == "__main__":
        app.run(debug=True)
    
    ```
    
3. **Realizar una petición con `curl`:**
    
    ```
    curl -X GET "http://127.0.0.1:5000/data" -H "Authorization: Bearer mi_clave_secreta"
    
    ```
    

---

### **Notas importantes**

- **No incluyas claves de API en el código**. Usa variables de entorno.
- **El prefijo `Bearer`** indica que el token es de autenticación.
- **Si la API usa OAuth2**, los headers pueden incluir `Bearer <token>`.

---

# **¿Qué es el Web Scraping?**

El **Web Scraping** es el proceso de extraer información de páginas web de forma automatizada. Se utiliza para recopilar datos de sitios, como precios de productos, noticias o contenido de redes sociales.

---

## **¿Cómo hacer Web Scraping con `requests`?**

La librería `requests` permite hacer peticiones HTTP para obtener el contenido de una página web.

1. **Instalar `requests` con Pipenv**
    
    ```
    pipenv install requests
    
    ```
    
2. **Ejemplo básico de Web Scraping con `requests`**
    
    ```python
    import requests
    
    url = "https://example.com"  # Página de ejemplo
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.text)  # Muestra el HTML de la página
    else:
        print(f"Error: {response.status_code}")
    
    ```
    

---

### **¿Cómo extraer datos de una web?**

El HTML devuelto por `requests` es un texto plano. Para analizarlo y extraer información, se usa una librería como **BeautifulSoup**.

1. **Instalar BeautifulSoup**
    
    ```
    pipenv install beautifulsoup4
    
    ```
    
2. **Extraer datos específicos de una página**
    
    ```python
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://example.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    
        # Extraer el título de la página
        title = soup.find("title").text
        print(f"Título de la página: {title}")
    
        # Extraer todos los enlaces
        links = soup.find_all("a")
        for link in links:
            print(link.get("href"))
    else:
        print(f"Error: {response.status_code}")
    
    ```
    

---

### **Notas importantes**

- Algunas páginas bloquean el scraping; usa **headers** para simular un navegador:
    
    ```python
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    ```
    
- Si la web usa JavaScript para cargar datos, `requests` no es suficiente; necesitarás **Selenium**.

---

# Excel - Python

La librería `openpyxl` en Python se utiliza para **leer, escribir y modificar archivos Excel** en el formato **XLSX**. Es una de las opciones más populares para trabajar con hojas de cálculo en Python.

## 📌 ¿Qué puedes hacer con `openpyxl`?

1. **Crear archivos Excel** desde cero.
2. **Abrir y modificar archivos existentes** sin alterar otros datos del archivo.
3. **Escribir datos en celdas** y aplicar formatos como negritas, colores y bordes.
4. **Leer datos de hojas de cálculo**, accediendo a celdas específicas o recorriendo filas y columnas.
5. **Manipular hojas** (crear, eliminar, renombrar y mover).
6. **Aplicar estilos y formatos** (colores, tamaños de fuente, alineación, etc.).
7. **Manejar fórmulas** dentro de las celdas.
8. **Insertar imágenes y gráficos** en las hojas de cálculo.

---

## 📌 Instalación con Pipenv

Para usar `openpyxl`, primero debes instalarlo dentro de tu entorno de `pipenv`:

```
pipenv install openpyxl

```

---

## 📌 Ejemplo Básico: Crear un Archivo Excel

Aquí tienes un código que **crea un archivo Excel y escribe datos en él**:

```python
from openpyxl import Workbook

# Crear un nuevo libro de trabajo y hoja activa
wb = Workbook()
ws = wb.active

# Escribir datos en celdas
ws['A1'] = "Hola"
ws['B1'] = "Mundo"
ws['A2'] = 42
ws['B2'] = 3.14

# Guardar el archivo
wb.save("ejemplo.xlsx")

```

Este código genera un archivo `ejemplo.xlsx` con los valores en las celdas `A1`, `B1`, `A2` y `B2`.

---

## 📌 Ejemplo: Leer un Archivo Excel Existente

Si quieres **leer los datos de un archivo Excel**, puedes hacerlo así:

```python
from openpyxl import load_workbook

# Cargar un archivo Excel existente
wb = load_workbook("ejemplo.xlsx")
ws = wb.active

# Leer valores de celdas
print(ws['A1'].value)  # Hola
print(ws['B1'].value)  # Mundo
print(ws['A2'].value)  # 42
print(ws['B2'].value)  # 3.14

```

---

# Selenium - Pruebas automáticas

Selenium es una biblioteca de Python (y otros lenguajes) que permite automatizar la interacción con navegadores web. Se usa principalmente para pruebas automatizadas en aplicaciones web, pero también puede emplearse para web scraping avanzado.

## ¿Cómo funciona Selenium?

Selenium interactúa con el navegador como si fuera un usuario real, permitiéndote:

- Abrir un navegador y navegar a una URL.
- Completar formularios y hacer clic en botones.
- Extraer información de una página web.
- Ejecutar scripts de JavaScript.
- Simular desplazamientos y otras interacciones.

### Ejemplo de caso de uso:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar el WebDriver para Chrome (descargar ChromeDriver y colocar su ruta)
driver = webdriver.Chrome()

# Abrir Google
driver.get("https://www.google.com")

# Buscar "Selenium Python"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Esperar que carguen los resultados
time.sleep(2)

# Obtener los títulos de los resultados
titles = driver.find_elements(By.CSS_SELECTOR, "h3")

# Imprimir los títulos
for title in titles:
    print(title.text)

# Cerrar el navegador
driver.quit()

```

## Instalar la versión de navegador para automatización

Sí, para usar **Selenium con Google Chrome**, necesitas descargar **ChromeDriver**, que es el WebDriver que permite que Selenium controle el navegador. Aquí están los pasos detallados:

---

### 🔹 **1. Instalar Selenium en tu entorno con Pipenv**

Abre una terminal en tu proyecto y ejecuta:

```
pipenv install selenium

```

Esto agregará Selenium a tu entorno virtual administrado por Pipenv.

---

### 🔹 **2. Descargar ChromeDriver**

Selenium necesita un WebDriver que sea compatible con la versión de tu Google Chrome.

### 🔹 **Verificar la versión de Chrome**

Abre Google Chrome y en la barra de direcciones escribe:

```
chrome://settings/help

```

Aquí verás la versión exacta de tu navegador.

### 🔹 **Descargar ChromeDriver compatible**

- Ve a la página oficial:
    
    👉 [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
    
- Descarga la versión que coincida con tu versión de Chrome.
- Extrae el archivo y ubica `chromedriver.exe` en una ruta accesible.

---

### 🔹 **3. Configurar Selenium para usar ChromeDriver**

Si ChromeDriver está en tu `PATH`, Selenium lo encontrará automáticamente. Si no, debes especificar su ruta.

### **Ejemplo de código con Selenium y ChromeDriver**

```python
from selenium import webdriver

# Si ChromeDriver está en el PATH, solo usa webdriver.Chrome()
# Si no, especifica la ruta al ejecutable de ChromeDriver:
driver = webdriver.Chrome()

# Abrir Google
driver.get("https://www.google.com")

# Imprimir el título de la página
print("Título de la página:", driver.title)

# Cerrar el navegador
driver.quit()

```

---

### 🔹 **4. Solucionar problemas comunes**

Si tienes errores, verifica:

1. Que tu versión de **ChromeDriver** coincida con la versión de **Google Chrome**.
2. Que ChromeDriver esté en una ubicación accesible.
3. Si obtienes un error de permisos en Linux/macOS, dale permisos de ejecución con:
    
    ```
    chmod +x chromedriver
    
    ```
    
4. Si ChromeDriver no está en el `PATH`, especifica la ruta directamente en el código:
    
    ```python
    driver = webdriver.Chrome(executable_path="C:/ruta/a/chromedriver.exe")
    
    ```
    

---