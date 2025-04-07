import requests
from bs4 import BeautifulSoup

url = "https://www.stackoverflow.com/questions"

response = requests.get(url)  # Realiza la solicitud HTTP
texto = response.text  # Obtiene el contenido de la respuesta pasado a texto
# Crea el objeto BeautifulSoup y analiza el HTML
soup = BeautifulSoup(texto, "html.parser")
# Selecciona todos los elementos con la clase "s-post-summary"
questions = soup.select(".s-post-summary")

for question in questions:
    # print(question)  # Imprime el elemento de la pregunta
    # Selecciona el título de la pregunta
    title = question.select_one(".s-link").get_text()
    # Imprime el título de la pregunta, .strip hace que se eliminen los espacios en blanco al principio y al final
    users = question.select_one(".s-user-card--link").get_text()
    print(f"User: {users.strip()} \nTitle: {title.strip()}")
    print("-" * 40)  # Imprime una línea separadora
