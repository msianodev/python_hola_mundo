# Control de Flujo

# Variables 2.0

Desempaquetado de variables, creamos los datos de una variable tomados de una tupla

```python
datos = ("Matias","Siano")
nombre, apellido = datos
```

formas de crear tuplas, se crean datos de solo lectura, optimiza mejor la memoria en diferencia con una lista.

```python
#creando tuplas con tuple()
tupla = tuple(["dato1", "dato2"])
print(tupla) #output dato1, dato2

#creado tuplas simple sin parentesis
tupla = "dato1", "dato2"
print(tupla) #output dato1, dato2
```

# Bucle for()

```python
#recorrer una lista con el bucle for
animales = ["perro","gato", "oso", "pajaro"]
for animal in animales:
	print(f'La variable animal es: {animal}')
#Output: perro, gato, oso, pajaro

numeros = [10,25,75,47]
for numero in numeros:
	resultado = numero*10
	print(resultado)
#Output: 100,250, 750, 470

#iterando dos listas en un solo for
for numero, anumal in zil(animales, numeros):
	print(f'Recorriendo lista animales: {animal}')
	print(f'Recorriendo lista numeros: {numero}')
#Output: perro, 100, gato, 250, oso, 750, pajaro, 470

#Recorro la lista por rango
for num in range(20, 30): #desde 20 inclusive, hasta 30 sin incluir
	print(num)
#Output: 20,21,22,23,24,25,26,27,28,29

#Recorrer una lista con indice
numeros = [10,25,75,47]
for num in enumerate(numeros): #recorre el numero enumerándo la posicion de la lista
	print(num)
#Output: (0,10),(1,25)(2,75)(3,47)

#Esto tambien funciona con las tuplas

#Recorrer un diccionario
diccionario = {
    "nombre" : "Matias",
    "apellido" : "Garcia",
    "edad" : 28
}
for key in diccionario:
	print(key)
#Output: nombre, apellido, dni (muestra la clave, sio ponemos 'value' muestra 
#solo los valores)
#si ponemos diccionario.items te lista las claves y los valores

#imprimir diccionario completo
for key in diccionario.items():
    print(key)
#Output:('nombre', 'Matias') ('apellido', 'Garcia') ('edad', 28)

#imprimir diciccionario completo
for key in diccionario:
    print(key, ":", diccionario[key])
#nombre : Matias apellido : Garcia edad : 28
```

# Bucle while()

```python
contador = 0
while contador < 10:
	print(contador)
	contador+=1
#Output; 0,1,2,3,4,5,6,7,8,9

```