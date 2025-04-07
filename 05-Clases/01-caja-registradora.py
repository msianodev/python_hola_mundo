# Ejercicio 1: Clase Caja Registradora

# Descripción:
# Este ejercicio implementa una clase Caja Registradora para gestionar productos y pagos en una tienda.
# La clase permite realizar las siguientes acciones:
# Agregar productos con su nombre y precio.
# Calcular el total de los productos agregados.
# Calcular el cambio basado en un pago proporcionado.
# Listar los productos añadidos.
# Limpiar la lista de productos después de realizar el pago.
#
# Propiedades:
# productos: Lista de diccionarios que contiene los productos agregados con su nombre y precio.

# Métodos:
# 1.__init__(): Inicializa una nueva instancia de la clase con una lista vacı́a de productos.
# 2.agregar_producto(nombre, precio): Agrega un producto a la lista de productos especificando su nombre y precio.
# 3.obtener_total(): Calcula y devuelve el total de los precios de los productos en la lista.
# 4.dar_cambio(pago): Calcula y devuelve el cambio basado en el pago proporcionado.
# Si el pago es insuficiente,lanza un mensaje indicando el problema. Limpia la lista de productos después de calcular elcambio.
# 5.listar_productos(): Devuelve la lista actual de productos agregados.
#
# Pruebas:
# 1.Agregar productos y obtener total:
# 2.Agregar los productos Manzana con precio de 0.5 y Pan con precio de 1.0.
# 3.Verificar que el total sea 1.5.
# 4.Calcular cambio:
# 5.Al pagar con 2.0, elcambio debe ser 0.5.
# 6.Si se paga con 1.0, debe lanzar se una excepción indicando pago insuficiente.
# 7.Listar productos:
# 8.Los productos en la lista deben ser Manzana y Pan.
# 9.Después de pagar, la lista de productos debe quedar vacı́a.
#
# Datos de prueba y salida esperada:
# [{'nombre': 'Manzana', 'precio': 0.5}, {'nombre': 'Pan', 'precio': 1.0}]
# Total: 1.5
# Cambio: 0.5
# []

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


caja = CajaRegistradora()
caja.agregar_producto('Manzana', 0.5)
print("Total: ", caja.obtener_total())

caja.agregar_producto('Pan', 1.0)
print("Total: ", caja.obtener_total())

print(caja.listar_productos())
print("Total: ", caja.obtener_total())
print("Cambio: ", caja.dar_cambio(2.0))
print(caja.listar_productos())
