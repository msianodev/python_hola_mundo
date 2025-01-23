print("Conversor de temperaturas")
x = float(input("Introduce la temperatura en grados Celsius: "))

x = x * 9/5 + 32 # Fórmula de conversión de grados Celsius a Fahrenheit

print(f"La temperatura en grados Fahrenheit es: {x}")

x = x + 273.15 # Fórmula de conversión de grados Fahrenheit a Kelvin

print(f"La temperatura en grados Kelvin es: {x}")
