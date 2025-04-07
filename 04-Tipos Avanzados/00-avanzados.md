# Tipos Avanzados

# Listas

Una lista es una colección ordenada de elementos que puede contener diferentes tipos de datos. Las listas son mutables, lo que significa que puedes cambiar sus elementos después de haberlas creado.

```python
mi_lista = [1, 2, 3, "cuatro", 5.0]
numeros = [1, 2, 3, 4] # Numeros
letras = ["a", "b", "c"] # Lista de letras
palabras = ["hola", "mundo", "aprendiendo", "python"] # Lista de Palabras
booleans = [False, True, True, False] # Lista de booleanos
matriz = [[0, 1],[1, 0]] # Lista que contiene 2 listas dentro.
ceros = [0] * 10 # es una lista de diez elementos que contienen cero = [0,0,0,0,0,0,...]
alfanumerico = numeros + letras # Concatena las 2 listas en una lista global.
rango = list(range(10)) # Crea una lista de 10 elementos del 0 al 9.
rango = list("hola mundo") # Crea una lista con los caracteres del string
# ['h','o','l','a',' ','m','u','n','d','o']
```

**Métodos comunes de listas:**

- `append(x)`: Agrega un elemento al final de la lista.
- `insert(i, x)`: Inserta un elemento en una posición específica.
- `remove(x)`: Elimina la primera aparición de un elemento.
- `pop(i)`: Elimina y retorna el elemento en la posición especificada.
- `sort()`: Ordena los elementos de la lista.

```python
mi_lista.append(6)
print(mi_lista)  # [1, 2, 3, "cuatro", 5.0, 6]

```

## Manipulación de listas

```python
# Dada la siguiente lista de mascotas:
mascotas = ["perros","gatos","canarios","peces"]

print(mascotas[0]) # Accedo a la posición cero de la lista
#Output: "perros"

mascotas[0] = "Lagartija" # Cambio el valor de la variable en la posición cero

print(mascotas[:3]) # Accedo a las posiciones desde el cero sin especificar, 
# Hasta la posición 3 = ["Lagartija","gatos","canarios"] 0, 1 y 2 posiciones.

print(mascotas[-1]) # Accedo a las última posición del arreglo desde retroceso.
#Output: "peces"

print(mascotas[::2]) # Accedo a los elementos pares de la lista
#Output: "perros", "canarios"

print(mascotas[1::2]) # Accedo a los elementos pares de la lista empezando desde 
#la posicion 1
#Output: "gatos", "peces"

print(mascotas[1:3:2]) # Accedo a los elementos pares de la lista empezando desde 
#la posicion 1 y finalizandola en la 3.
#Output: "gatos", "peces"
```

## Desempaquetar Listas

```python
# Para descomponer los elementos de una lista se realiza de la siguiente manera:
numeros = [1, 2, 3]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)
# Output: 1, 2, 3

primero, *otros = numeros
print(primero) # Accedo al primer valor de números.
# El *otros funciona como un xarg o *args donde se almacenan el resto de los numeros
# de la lista
print(otros) # Output: [2, 3]

# Otros ejemplos con una lista mas larga:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15]
primero, segundo, *otros, penultimo, ultimo = numeros
# Puedo acceder a los elementos que desee de la lista
print(segundo, penultimo, otros)
# Output: 2, 14, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

## Iterando Listas

```python
# Dada la siguiente lista, se desea recorrer los elementos:

frutas = ["banana", "durazno", "naranja", "melon", "kiwi", "sandia", "frutilla"]

# El recorrido simple de una lista se realiza con un bucle for:
for fruta in frutas:
	print(fruta) # Output: banana

# Para que nos devuelva los índices de las listas se utiliza la funcion enumerate
for fruta in enumerate(frutas):
	print(fruta) # Output: (0, 'banana') -> también se denomina tupla

```

## Búsqueda de elementos

```python
# Dada la siguiente lista, se desea buscar el índice de un elemento:

marcas = ["coca-cola", "apple", "asus", "logitech", "samsung"]
print(marcas.index("apple")) # Output: 1

```

## Agregar y eliminar elementos

```python
# Para insertar valores en una lista se puede hacer de la siguiente manera
colores = [
		"rojo", 
		"amarillo", 
		"azul", 
		"verde", 
		"naranja" 
	]
	colores.insert(1, "violeta") # Establecemos el índice y luego el valor de la variable.
	print(colores)
	# Output: ['rojo', 'violeta', 'amarillo', 'azul', 'verde', 'naranja']
	
	
	# Para agregar al final de la lista
	colores.append("blanco")
	print(colores)
	# Output: ['rojo', 'violeta', 'amarillo', 'azul', 'verde', 'naranja', 'blanco']
	
	
	# Para eliminar un elemento (sólo elimina el primer elemento que encuentra en la lista)
	colores.remove("azul")
	print(colores)
	# Output: ['rojo', 'violeta', 'amarillo', '~~azul~~', 'verde', 'naranja', 'blanco']
	
	
	# Para eliminar el último elemento de la lista
	colores.pop() # Elimina el último sin especificar cuál sea.
	
	colores.pop(2) # Elimina el elemento correspondiente al índice en el argumento.
	del colores[3] # Elimina el elemento correspondiente al índice mencionado.
	
	colores.clear() # Elimina todo el contenido de la lista.
```

## Ordenar elementos de la lista

```python
# Para ordenar los elementos de una lista se utiliza el siguiente método:

numeros = [4, 2, 17, 1, 3, 9]
numeros.sort() # Ordena de menor a mayor todos los elementos
print(numeros) # Output: [1, 2, 3, 4, 9, 17]

numeros.sort(reverse = True) # Ordena de mayor a menor todos los elementos
print(numeros) # Output: [17, 9, 4, 3, 2, 1]

sorted(numeros) # Genera una nueva lista ordenada de menor a mayor.
sorted(numeros, reverse=True) # Genera una nueva lista ordenada de mayor a menor
```

## Funciones Lambda, funciones anónimas

```python
# Pueden realizarse ordenamientos de una forma no convencional

usuarios = [
	["Juan", 4],
	["Mateo", 2],
	["Silvia", 6],
]

def ordena(elemento):
	return elemento[1]
	
usuarios.sort(key=ordena, reverse=True) }
# Ordena no lleva '()' porque el método de .sort se encarga de pasarle el elemento
print(usuarios)

# Funciones lambda para mejorar este comportamiento de ordenación:
usuarios = [
	["Juan", 4],
	["Mateo", 2],
	["Silvia", 6],
]

~~def ordena(elemento):
	return elemento[1]~~
	
usuarios.sort(key=lambda elem:elem[1] , reverse=True) }
# Se utiliza cuando tenemos que utilizar una función una única vez.
print(usuarios)
```

## Listas de comprensión

```python
# Las listas de comprensión se utilizan para reducir lineas de código.

autos= [
	["peugeot", 4],
	["ford", 2],
	["volkswagen", 6],
]

# De esta lista sólamente vamos a querer extraer el nombre de los autos.
# Vamos a transformar la lista de autos a una lista de nombres de autos.
# Convencionalmente se realizaría de la siguiente manera:

nombres_autos = [] # Declaro una nueva lista vacía
for auto in autos:
	nombres_autos.append(auto[0])
print(nombres_autos)

# Una forma elegante de mejorar esto es mediante las listas de comprensión:

# nombres_autos = [expresion for item in items]

# items: Es la lista que estamos iterando
# item: Es el nombre de cada elemento de la iteración
# expresion: Es la transformación que le vamos a aplicar 
#  a los elementos para que sean nuevamente asignados a la lista de nombres_autos

# se lo conoce como: map
nombres_autos = [nombre[0] for auto in autos]
# nombre[0] es el elemento de nombre que queremos obtener.
print(nombres_autos) # Output: peugeot, ford, volkswagen

# Otra forma para usar estas listas de compresión es para realizar filtros:
# Se lo conoce como: filter
nombres_autos = [auto for auto in autos if auto[1] > 2]
print(nombres_autos) # Output: peugeot, volkswagen
```

# Map & Filter

Por convención es mejor utilizar listas de comprensión pero podemos encontrar código realizado con map y filter

```python
usuarios = ['Mati', 'John', 'Mela']
nombres = list(map(lambda usuario: usuario[0], usuarios))
print (nombres) # Output: [Mati, John, Mela]

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios) # Output: [Mela, 3]

```

# Tuplas

Las tuplas son listas de elementos pero con la particularidad de que no son editables ni modificables. Una vez establecida la tupla no será posible modificar sus elementos

```python
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros) # Output: (1, 2, 3, 4, 5, 6)

punto = tuple([1,2]) # Una forma de transformar de una lista a una tupla

# Se pueden utilizar todas las operaciones de listas menos las que la modifican
menosNumeros = numeros[:2]
print(menosNumeros) # Output: (1, 2)

primero, segundo, *otros = numeros
print(primero, segundo)
print(otros)
# Output: 1 2
# Output: [3, 4, 5, 6]
```

# Sets

Son un conjunto o grupo.

Es una colección de datos que no se puede repetir y que no está ordenada

```python
primer = {1, 1, 2, 2, 2, 3, 4}
print(primer) # Output: 1, 2, 3, 4

# Posee el mismo comportarmiento que las listas
primer.add(5)
primer.remove(1)

# Transformar una lista a un set:
primer = {1, 1, 2, 2, 2, 3, 4}
segundo = [1 ,3, 4]

segundoSet = set(segundo)
print(segundo) # Output: {1, 3, 4}
```

### Operadores de Set

```python
#Dados los siguientes sets:
primer = {1, 1, 2, 2, 2, 3, 4}
segundo = {1, 1, 4, 4, 5, 5, 6}

# Union
print(primer | segundo) # Output: {1, 2, 3, 4, 5, 6}

# Intersección
print(primer & segundo) # Output: {1, 4}

# Diferencia
print(primer - segundo) # Output: {2, 3}

# Diferencia Simétrica
print(primer ^ segundo) # Output: {2, 3, 5, 6}
```

# Diccionarios

Los diccionarios en python son un conjunto de pares clave-valor que se almacenan en una variable

```python
punto = {"x": 10, "y": 5}
print(punto) # Output: {'x': 10, 'y': 5}

# Acceder a un valor de estas llaves:
print(punto["x"]) # Output: 10

# Agregar información al diccionario:
punto["z"] = 12
print(punto) # Output: {'x': 10, 'y': 5, 'z': 12}

# Buscar elementos en un diccionario:
if 'h' in punto:
	print(punto['h'])

# Buscar elementos con un método nativo
print(punto.get("y")) # Output: 5
print(punto.get("asd")) # Output: None
print(punto.get("asd", 99)) # Output: 99

# Eliminar un elemento del diccionario
del punto ["x"]
print(punto) # Output: {'y': 5, 'z': 12}
del (punto ["y"])
print(punto) # Output: {'z': 12} 

# Iterar dentro de un diccionario:
for valor in punto.items():
	print(valor)
# Output: ('x', 10) ('y': 5) ('z': 12)

# Uso típico de un diccionario:
autos = [
	{"id": 1, "marca": Toyota, "modelo": Corolla},
	{"id": 2, "marca": Ford, "modelo": Focus},
	{"id": 3, "marca": Ford, "modelo": Fiesta},
	{"id": 4, "marca": Volkswagen, "modelo": Amarok},	
]

# Acceder a las marcas de los autos:
for auto in autos:
	print(auto["marca"])
# Output: Toyota, Ford, Ford, Volkswagen

```

# Operador de des empaquetamiento

```python
lista = [1, 2, 3, 4]
print(lista) 

# Para poder imprimir cada elemento de la lista separadamente:
print(*lista) # Output: 1 2 3 4

# Sirve para cualquier tipo de dato iterable: listas, tuplas, diccionarios

punto1 = {"x": 19}
punto2 = {"y": 12}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto) # Output: {'x': 19, 'y': 12}

```

# Pilas y Filas

Una Fila es un comportamiento de elementos, FIFO (First-In, First-Out). Simula el comportamiento de una fila de supermercado.

Una Pila es un comportamiento de elementos, LIFO (Last-In, First-Out). Simula el comportamiento de una pila de libros.

### Operando Filas

```python
from collections import deque
	
fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
print(fila) # Output: deque([1, 2, 3, 4, 5])
fila.popleft() # Elimina elementos de a uno desde la izquierda

if not fila:
	print("fila vacía")

```

### Operando Pilas

```python
# Se ultiliza el mismo comportamiento que las listas pero de forma lógica de pila.

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila) # Output: [1, 2, 3]

ultimoElemento = pila.pop()
print(ultimoElemento) # Output: 3
```