# Ejercicio 6: Cálculo de Cambio
#
# Descripción
# Este programa calcula el cambio que debe darse al cliente según el pago y el total de la cuenta.
#
# Pruebas
# 1.Entrada: Total: 100, Pago: 100.
# Salida:" El cliente ha pagado el monto exacto. No se requiere cambio".
#
# 2.Entrada: Total: 50, Pago: 40.
# Salida: "El cliente ha pagado menos. Faltan 10.0 dólares".
#
# 3.Entrada: Total: 75, Pago: 100.
# Salida:" El cliente ha pagado demás. El cambio es 25.0 dólares”.

print("Calculo de Cambio")

total_cuenta = float(input("Ingrese el total de la cuenta: "))

pago_cliente = float(input("Ingrese el monto pagado por el cliente: "))

if total_cuenta <= 0 or pago_cliente <= 0:
    print("Ingrese un total y un pago validos.")
    exit()

if pago_cliente == total_cuenta:
    print("El cliente ha pagado el monto exacto. No se requiere cambio.")

elif pago_cliente < total_cuenta:
    print(f"El cliente ha pagado menos. Faltan cobrar $ {
          (total_cuenta - pago_cliente):.2f} dólares.")

else:
    print(f"El cliente ha pagado demás. El cambio es de $ {
          (pago_cliente - total_cuenta):.2f} dólares.")
