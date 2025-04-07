import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

# apikey = os.environ.get("SENDGRID_API_KEY") # Cambiamos la forma de obtener la API key
email = os.environ.get("SENDGRID_EMAIL")

# Creamos un objeto con el correo que vamos a enviar
mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="Prueba de envio de correo",
    html_content="<strong>Hola, este es un mensaje de prueba</strong>"
)

try:
    # Creamos un cliente de SendGrid
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    # Enviamos el correo
    response = sg.send(mensaje)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
