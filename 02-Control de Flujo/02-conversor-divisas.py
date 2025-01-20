# Ejercicio 2: Conversor de Divisas

# Descripción:
# Este programa convierte una cantidad de dinero de una divisa a otras.
# Divisas soportadas:
# USD(dólares estadounidenses),
# EUR(euros),
# MXN(pesosmexicanos).
#
# El usuario ingresa la cantidad y la divisa de origen,
# y el programa calcula las cantidades equivalentes en las otras divisas.
#
# Tasas de Conversión
# •1USD = 0.95EUR
# •1USD = 20.28MXN
# •1EUR = 21.36MXN
#
# Pruebas
# 1.Entrada:100USD.
# Salida: 95EUR, 2028MXN.
#
# 2.Entrada:100EUR.
# Salida:105.26USD, 2136MXN.
#
# 3.Entrada:100MXN.
# Salida:4.93USD,4.68EUR.
#
# 4.Entrada:Divisa no válida.
# Salida:"Divisa no válida.Porfavor,elige entre USD, EUR o MXN.”

print("Conversor de Divisas")
print("Divisas soportadas: USD, EUR, MXN")

# Solicitar la cantidad y la divisa de origen
cantidad = float(input("Ingresa la cantidad: "))
divisa = input("Ingresa la divisa de origen: ").strip().upper()

# Definir las tasas de conversión
TASA_USD_EUR = 0.95
TASA_USD_MXN = 20.28
TASA_EUR_MXN = 21.36

# Realizar la conversión
if divisa == "USD":
    cantidad_eur = cantidad * TASA_USD_EUR
    cantidad_mxn = cantidad * TASA_USD_MXN
    print(f"{cantidad} USD son {cantidad_eur:.2f} EUR, {cantidad_mxn:.2f} MXN")
elif divisa == "EUR":
    cantidad_usd = cantidad / TASA_USD_EUR
    cantidad_mxn = cantidad * TASA_EUR_MXN
    print(f"{cantidad} EUR son {cantidad_usd:.2f} USD, {cantidad_mxn:.2f} MXN")

elif divisa == "MXN":
    cantidad_usd = cantidad / TASA_USD_MXN
    cantidad_eur = cantidad / TASA_EUR_MXN
    print(f"{cantidad} MXN son {cantidad_usd:.2f} USD, {cantidad_eur:.2f} EUR")
else:
    print("Divisa no válida. Por favor, elige entre USD, EUR o MXN.")
