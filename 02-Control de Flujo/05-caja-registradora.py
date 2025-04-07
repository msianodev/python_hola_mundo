# Ejercicio 5: Caja Registradora
#
# Descripción Este programa simula una caja registradora que acumula el precio de los productos
# ingresados por el usuario.
#
# Pruebas
# 1.Ingresar los precios de 10, 20 y 30 y luego fin.
# Salida:"El total a pagar es: 60.00 dólares".
#
# 2.Ingresar "fin" sin precios.
# Salida:"El total a pagar es: 0.00 dólares”

print("Caja Registradora")

TOTAL = 0
SALIDA = "hola"
print("Ingrese el precio de los productos o escriba 'fin' para terminar.")

while SALIDA != "fin":
    precio = float(input("Precio del producto: "))

    if precio >= 0:
        TOTAL += precio

    elif precio == "fin":
        break
    else:
        print("Ingrese un precio valido.")
        break
    SALIDA = input("Escriba 'fin' para terminar: ").lower().strip()


print(f"El total a pagar es: {TOTAL:.2f} dólares")
