from holamundoplayer import player

import requests
# pip install requests
#
# requests es una librería que permite hacer peticiones HTTP de manera sencilla.
#
# GET: Solicita datos de un recurso específico.
# POST: Envía datos para ser procesados por un recurso.
# PUT: Actualiza un recurso.
# DELETE: Elimina un recurso.
# PATCH: Actualiza parcialmente un recurso.
# HEAD: Solicita datos de un recurso específico, pero sin el cuerpo de la respuesta.
# OPTIONS: Devuelve los métodos HTTP que el servidor soporta para un URL específico.

r = requests.get('https://www.google.com')
print(r.status_code)  # 200 si la petición fue exitosa
print(r.ok)  # True si el status_code es 200
print(r)  # Respuesta completa
print(r.headers)  # Headers de la respuesta

p = player.Player()
p.play("La Bamba")
