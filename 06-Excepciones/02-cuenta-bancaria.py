# Ejercicio 2: Clase de Cuenta Bancaria
#
# Descripción
# Aquı́ se implementa una clase CuentaBancaria que maneja depósitos, retiros y saldos,
# con excepciones personalizadas para manejar errores como retiros de cantidades negativas o superiores
# al saldo disponible.
#
# Datos de Prueba
# try:
#   cuenta = CuentaBancaria("123456789", "Juan Perez", 1000)
#   cuenta.mostrar_saldo()
#   cuenta.depositar(500)
#   cuenta.retirar(2000)
# except ErrorRetiro as e:
#   print(e)
#
# try:
#   cuenta.retirar(-100)
# except ErrorRetiro as e:
#   print(e)
#
# Salida Esperada
# Saldo actual: 1000
# Depósito exitoso. Nuevo saldo: 1500
# ('Fondos insuficientes para realizar el retiro.', 401)
# ('La cantidad a retirar debe ser positiva.', 400)

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con operaciones de depósito, retiro y consulta de saldo.
    """

    def __init__(self, numero_cuenta, nombre_titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo

    def mostrar_saldo(self):
        """
        Muestra el saldo actual de la cuenta.
        """
        print(f"Saldo actual: {self.saldo}")

    def depositar(self, cantidad):
        """
        Realiza un depósito en la cuenta.

        :param cantidad: Cantidad a depositar.

        """
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        """
        Realiza un retiro en la cuenta.

        :param cantidad: Cantidad a retirar.
        :raise ErrorRetiro: Si la cantidad a retirar es negativa o supera el saldo disponible

        """
        if cantidad < 0:
            raise ErrorRetiro("La cantidad a retirar debe ser positiva.", 400)
        if cantidad > self.saldo:
            raise ErrorRetiro(
                "Fondos insuficientes para realizar el retiro.", 401)
        self.saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")


class ErrorRetiro(Exception):
    """
    Excepción personalizada para manejar errores en los retiros de la cuenta.
    """

    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo


try:
    cuenta = CuentaBancaria("123456789", "Juan Perez", 1000)
    cuenta.mostrar_saldo()
    cuenta.depositar(500)
    cuenta.retirar(200)
    # cuenta.retirar(2000)
    # cuenta.retirar(-100)
except ErrorRetiro as e:
    print(e)
