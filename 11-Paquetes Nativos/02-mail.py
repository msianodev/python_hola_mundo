from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# Multipurpose Internet Mail Extensions: Es un estandar de internet que extiende el formato de correo para soportar texto enriquecido, adjuntos, etc.
mensaje = MIMEMultipart()

mensaje['from'] = 'Remitente'
mensaje['to'] = 'Destinatario'
mensaje['subject'] = 'Asunto'
cuerpo_mensaje = MIMEText('Contenido del mensaje')
mensaje.attach(cuerpo_mensaje)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Identifica con el servidor de correo
    smtp.starttls()  # Protocolo de encriptación. TLS: Transport Layer Security

    smtp.login("pepito@gmail.com", "12345")
    smtp.send_message(cuerpo_mensaje)
