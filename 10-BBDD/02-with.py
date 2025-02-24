import sqlite3

# Creamos la conexión a la base de datos, si no existe python lo crea
with sqlite3.connect("app.db") as conn:
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

    # Insertar valores en la tabla
    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        ('Matias', 25),

    )

    # Insertar varios valores en la tabla
    users = [
        ('Javier', 30),
        ('Luis', 40),
        ('Maria', 50),
    ]
    cursor.executemany(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        users
    )

    cursor.execute("SELECT name FROM users WHERE age = ?", (30,))
    user = cursor.fetchone()
    print(f'El usuario de 30 años es: {user}')

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
