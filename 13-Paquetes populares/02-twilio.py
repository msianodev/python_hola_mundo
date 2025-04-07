import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_AUTH_TOKEN")
phone = os.environ.get("TWILIO_PHONE_NUMBER")

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola, este es un mensaje de prueba",
    from_=phone,
    to="+123456789"  # Cambia este número por el tuyo
)
