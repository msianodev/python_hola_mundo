# Ejercicio 3: Calculadora de Cambio
#
# ¿Cómo funciona?
#
# Este programa calcula el cambio que se debe devolver a un cliente después de una compra.
#
# 1.Solicita al usuario dos datos:
# 2.Cantidad de dinero entregada por el cliente.
# 3.Costo del producto.
# 4.Calcula el cambio restando el costo del producto al dinero entregado.
# 5.Muestra el cambio a devolver.
#
# Entradas
# •Dinero entregado por el cliente.
# •Costo del producto.
#
# Salidas
# •Cambio a devolver.
#
# Ejemplos
# •Entrada:50,30 -> Cambio:20.0
# •Entrada:100,75.5 -> Cambio:24.5
# •Entrada:20,20 - >Cambio:0.0

print("Calculadora de Cambio")
costo_producto = float(input("Ingrese el costo del producto: $ "))
dinero_entregado = float(
    input("Ingrese la cantidad de dinero entregada por el cliente: $ "))

cambio = dinero_entregado - costo_producto

print(f"Cambio a devolver: $ {cambio:.2f}")
