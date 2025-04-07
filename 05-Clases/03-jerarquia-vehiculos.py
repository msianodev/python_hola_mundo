# Ejercicio 3: Jerarquía de Clases para Vehículos
#
# Descripción: Este ejercicio define una jerarquı́a de clases para representar diferentes tipos de vehı́culos.
# Se implementa una clase base Vehiculo con atributos comunes y subclases especializadas para coches, motos y bicicletas.
#
# Clases
# 1.Vehiculo(Clase Base): Representa un vehı́culo genérico con los atributos:
# 2.marca: Marca del vehı́culo.
# 3.modelo: Modelo del vehı́culo.
#
# Métodos:
# descripcion(): Devuelve una descripción en formato "Marca: <marca>, Modelo: <modelo>".
# Coche(SubclasedeVehiculo): Especializa la clase base para coches y redefine el método descripcion() para incluir el prefijo "Coche - ".
# Moto(SubclasedeVehiculo):Especializa la clase base para motos y redefine el método descripcion() para incluir el prefijo "Moto - ".
# Bicicleta(SubclasedeVehiculo):Especializa la clase base para bicicletas y redefine el método descripcion() para incluir el prefijo "Bicicleta - ".
#
# Pruebas:
# 1.Crear instancias de cada tipo de vehı́culo con las siguientes marcas y modelos:
# 2.Coche:"Nissan", "Versa"
# 3.Moto:"Yamaha", "MT-07"
# 4.Bicicleta:"Giant", "Escape 3"
# 5.Llamar al método descripcion() en cada instancia y verificar la salida.
#
# Datos de prueba y salida esperada:
# Coche - Marca: Nissan, Modelo: Versa
# Moto - Marca: Yamaha, Modelo: MT-07
# Bicicleta - Marca: Giant, Modelo: Escape 3

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        self.descripcion = f'Marca: {self.marca}, Modelo: {self.modelo}'
        return self.descripcion


class Coche(Vehiculo):
    def descripcion(self):
        return f'Coche - {super().descripcion()}'


class Moto(Vehiculo):
    def descripcion(self):
        return f'Moto - {super().descripcion()}'


class Bicicleta(Vehiculo):
    def descripcion(self):
        return f'Bicicleta - {super().descripcion()}'


# Pruebas
coche = Coche('Nissan', 'Versa')
print(coche.descripcion())

moto = Moto('Yamaha', 'MT-07')
print(moto.descripcion())

bicicleta = Bicicleta('Giant', 'Escape 3')
print(bicicleta.descripcion())
