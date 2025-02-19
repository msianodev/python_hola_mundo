# Ejercicio 1: Conversor de Temperatura

# ¿Cómo funciona?

# Este programa convierte una temperatura dada en grados Celsius a dos escalas diferentes:
# Fahrenheit y Kelvin.

# 1.Pide al usuario que ingrese una temperatura en grados Celsius.

# 2.Realiza las siguientes conversiones:

# 3.Celsius a Fahrenheit:(gradosCelsius*9/5)+32
# 4.Celsius a Kelvin:gradosCelsius+273.15

# Muestra las temperaturas convertidas en ambas escalas.

# Entradas
# Temperatura en grados Celsius(puede ser un número entero o decimal).

# Salidas
# 1.Temperatura en grados Celsius.
# 2.Temperatura en grados Fahrenheit.
# 3.Temperatura en grados Kelvin.

# Ejemplos
# •Entrada: 0 -> Fahrenheit: 32, Kelvin: 273.15
# •Entrada: 100 -> Fahrenheit: 212, Kelvin: 373.15
# •Entrada: -40 -> Fahrenheit: -40, Kelvin:233.15
# •Entrada: 37 -> Fahrenheit:98.6, Kelvin:310.15

print("Conversor de Temperatura")
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (temperatura * 9/5) + 32
kelvin = temperatura + 273.15

print(f"Temperatura en grados Celsius: {temperatura}")
print(f"Temperatura en grados Fahrenheit: {fahrenheit:.2f}")
print(f"Temperatura en grados Kelvin: {kelvin:.2f}")
