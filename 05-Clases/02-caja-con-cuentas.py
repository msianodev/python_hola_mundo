# Ejercicio 2 :Clases Caja Registradora y Cuentas
#
# Descripción:
# Este ejercicio introduce la clase Caja Registradora, que permite gestionar productos y pagos,
# y la clase Cuentas, que registra múltiples cuentas, calcula el total de ventas y determina el ticket promedio.
#
# Clase Caja Registradora
# Atributos:
# productos: Lista de productos agregados, cada uno representado como un diccionario con nombre y precio.
#
# Métodos:
# 1.__init__(): Inicializa una lista vacı́a de productos.
# 2.agregar_producto(nombre, precio): Agrega un producto especificando su nombre y precio.
# 3.obtener_total(): Calcula y devuelve el total de los precios de los productos en la lista.
# 4.dar_cambio(pago): Calcula y devuelve el cambio basado en el pago proporcionado.
# Si el pago es insuficiente, devuelve un mensaje de error.
# Limpia la lista de productos tras calcular elcambio.
# 5.listar_productos(): Devuelve la lista actual de productos agregados.
#
#
# Clase Cuentas
# Atributos:
# cuentas: Lista de cuentas registradas, cada una con sus productos y total.
#
# Métodos:
# 1.__init__(): Inicializa una lista vacı́a de cuentas.
# 2.agregar_cuenta(caja_registradora): Agrega una cuenta a la lista basada en los productos y el total de una instancia de Caja Registradora.
# 3.obtener_total_cuentas(): Calcula y devuelve el total de todas las cuentas registradas.
# 4.obtener_ticket_promedio(): Calcula y devuelve el ticket promedio de todas las cuentas. Si no hay cuentas, devuelve 0.
# 5.listar_cuentas(): Devuelve la lista de cuentas registradas.
#
# Pruebas:
# 1.Agregar productos y registrar cuentas:
# 2.Agregar productos y registrar cuentas en Cuentas.
# 3.VeriCicar el total de ventas y el ticket promedio del dı́a.
# 4.Listar las cuentas registradas.

class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def obtener_total(self):
        return sum([producto['precio'] for producto in self.productos])

    def dar_cambio(self, pago):
        total = self.obtener_total()
        if pago < total:
            raise ValueError('Pago insuficiente')
        self.productos = []
        return pago - total

    def listar_productos(self):
        return self.productos


class Cuentas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, caja_registradora):
        self.cuentas.append({'productos': caja_registradora.listar_productos(
        ), 'total': caja_registradora.obtener_total()})

    def obtener_total_cuentas(self):
        return sum([cuenta['total'] for cuenta in self.cuentas])

    def obtener_ticket_promedio(self):
        if len(self.cuentas) == 0:
            return 0
        return self.obtener_total_cuentas() / len(self.cuentas)

    def listar_cuentas(self):
        return self.cuentas


caja = CajaRegistradora()
registro_cuentas = Cuentas()

caja.agregar_producto('Manzana', 0.5)
caja.agregar_producto('Pan', 1.0)
print(caja.listar_productos())
print("Total: ", caja.obtener_total())
registro_cuentas.agregar_cuenta(caja)

print("Cambio: ", caja.dar_cambio(2.0))
print(caja.listar_productos())

caja.agregar_producto('Leche', 1.5)
print("Total:", caja.obtener_total())

registro_cuentas.agregar_cuenta(caja)
print("Cambio:", caja.dar_cambio(3.0))
print(caja.listar_productos())

caja.agregar_producto('Huevos', 2.0)
caja.agregar_producto('Queso', 3.0)
caja.agregar_producto('Jamon', 4.0)
caja.agregar_producto('Pan', 1.0)

print("Total:", caja.obtener_total())

registro_cuentas.agregar_cuenta(caja)
print("Cambio:", caja.dar_cambio(10.0))

ticket_promedio_dia = registro_cuentas.obtener_ticket_promedio()
corte_dia = registro_cuentas.obtener_total_cuentas()
cuentas = registro_cuentas.listar_cuentas()

print("Cuentas del día:", cuentas)
print(f"El ticket promedio del día es de: {ticket_promedio_dia}")
print(f"El total de ventas del día es de: {corte_dia}")
