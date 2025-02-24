import sqlite3

# Creamos la conexión a la base de datos, si no existe python lo crea
conn = sqlite3.connect("app.db")
cursor = conn.cursor()  # Creamos un cursor

# Creamos una consulta SQL
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """
)

# Comprometer los cambios en la bbdd
conn.commit()  # si no se hace, no se guardan los cambios

conn.close()  # Cerramos la conexión
