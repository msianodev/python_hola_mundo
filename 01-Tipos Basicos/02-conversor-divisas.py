# Ejercicio 2: Conversor de Divisas
#
# ¿Cómo funciona?
#
# Este programa calcula cuánto costarı́a un producto en diferentes monedas extranjeras
# a partir de una cantidad ingresada en moneda local.

# 1.Solicita al usuario que ingrese una cantidad en su moneda local.

# 2.Convierte la cantidad a las siguientes monedas:
# 3.USD:cantidad*0.050
# 4.EUR:cantidad*0.047
# 5.GBP:cantidad*0.039
# 6.JPY:cantidad*7.71 7.

# Muestra los resultados de cada conversión.

# Entradas
# Cantidad en moneda local.

# Salidas
# Cantidad equivalente en USD, EUR, GBP y JPY.
#
# Ejemplos
# •Entrada: 100 -> USD:5.00, EUR:4.70, GBP:3.90, JPY:771.00
# •Entrada: 250 -> USD:12.50, EUR:11.75, GBP:9.75, JPY:1927.50
# •Entrada: 50 -> USD:2.50, EUR:2.35, GBP:1.95, JPY:385.50

print("Conversor de Divisas")
cantidad = float(input("Ingrese la cantidad en su moneda local: $ "))

usd = cantidad * 0.050
eur = cantidad * 0.047
gbp = cantidad * 0.039
jpy = cantidad * 7.71

print(f"Cantidad en USD: {usd:.2f}")
print(f"Cantidad en EUR: {eur:.2f}")
print(f"Cantidad en GBP: {gbp:.2f}")
print(f"Cantidad en JPY: {jpy:.2f}")
