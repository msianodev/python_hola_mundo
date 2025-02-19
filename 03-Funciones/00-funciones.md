# Funciones

# Funciones `def()`

```python
#funcion simple
def saludar()
	print("Hola, como estas?")
saludar()
#Output: "hola, como estas?"

#utilizar el operador * como argunmento (*args)
def suma(nombre, *numeros):
	return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
resultado = suma("Juan", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(resultado)
#Output: Juan, la suma de tus numeros es: 55
```

## Parámetros y Argumentos

En Python (y en la mayoría de lenguajes de programación), **los parámetros** son las variables que se definen en la declaración de una función, mientras que **los argumentos** son los valores concretos que se pasan a esa función cuando la invocas.

**Ejemplo sencillo:**

```python
def saludar(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}!")

saludar("Juan")  # "Juan" es el argumento

```

- **Parámetro**: `nombre` (lo que la función espera recibir; es como la “caja” vacía)
- **Argumento**: `"Juan"` (el valor real que colocamos dentro de esa “caja” al llamar la función)

De esta forma, cuando invocas la función `saludar("Juan")`, el valor `"Juan"` se asigna al parámetro `nombre`, y finalmente dentro de la función se imprime “Hola, Juan!”.

---

## Argumentos Opcionales vs Argumentos Nombrados

En Python, **los argumentos opcionales** son aquellos que tienen un valor por defecto en la definición de la función. Esto hace que no sea necesario proporcionarlos cada vez que se llama a la función.

Por otro lado, **los argumentos nombrados** (o *keyword arguments*) son aquellos a los que les indicas su nombre al momento de invocar la función. Esto te permite, por ejemplo, cambiar el orden en que envías los argumentos sin confundirlos.

**Ejemplo sencillo:**

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

# Al no especificar 'saludo', se usa su valor por defecto ("Hola").
saludar("Juan")               # Hola, Juan!

# Se indica explícitamente el valor del argumento 'saludo'.
saludar("Pedro", saludo="Hey")   # Hey, Pedro!

# Uso de argumentos nombrados en cualquier orden:
saludar(saludo="Buenos días", nombre="Lucía")  # Buenos días, Lucía!

```

1. **Argumento opcional**:
    - `saludo` tiene como valor por defecto `"Hola"`. Si no se proporciona otro valor, se utiliza el definido en la función.
2. **Argumentos nombrados**:
    - `saludar(nombre="Lucía", saludo="Buenos días")` indica el nombre de cada parámetro al llamar la función, lo que hace más claro el código y permite cambiar el orden de los argumentos.

### `xargs`

En Python, a menudo se utiliza la expresión **`*args`** (informalmente llamada `*xargs*` en algunos contextos) para referirse a **argumentos de longitud variable**. Esto significa que la función puede recibir una cantidad ilimitada de argumentos posicionales.

**Ejemplo simple:**

```python
def sumar_todo(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado1 = sumar_todo(1, 2, 3)       # 1 + 2 + 3 = 6
resultado2 = sumar_todo(5, 10, 15, 20) # 5 + 10 + 15 + 20 = 50

print(resultado1)  # 6
print(resultado2)  # 50

```

1. `args` actúa como una tupla que recoge todos los valores pasados después de los parámetros obligatorios (si los hubiera).
2. Puedes pasar tantos argumentos posicionales como necesites sin modificar la definición de la función.

### `kwargs`

En Python, se suele usar **`**kwargs`** (del inglés *keyword arguments*) para indicar que se recibirán un número variable de argumentos con nombre (o, dicho de otra forma, un número variable de *keyword arguments*). Todos estos argumentos se almacenan en un **diccionario** dentro de la función.

**Ejemplo simple:**

```python
def imprimir_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_informacion(nombre="Juan", edad=30, ciudad="Madrid")

def mi_funcion(**datos):
		print(datos["id"], datos["name"])
		
mi_funcion( id="23", 
						name="iphone", 
						descripcion="this is an iphone")
						
# { id=23 , name=iphone }

```

- Al definir la función como `def imprimir_informacion(**kwargs):`, cualquier argumento con nombre que le pases (por ejemplo, `nombre="Juan"`, `edad=30`) se guarda como parejas *clave: valor* en el diccionario `kwargs`.
- Dentro de la función, puedes acceder a cada uno de estos argumentos recorriendo el diccionario o directamente con `kwargs['nombre_de_argumento']`.

# Funciones lambda

Las funciones lambda son funciones anónimas, funciones que no tienen nombre

sintaxis: lambda `<parametros>:<expresion>`

```python
multiplicar_por_dos = lambda x:x*2
# es lo mismo que hacer:
def multiplicar_por_dos(x):
	return x*2
#Ahorra el abrir un bloque de código como lo seria una funcion
# es para hacer algo sencillo y rapido y retorna automáticamente

#usando filter con una funcion comun
numeros = [1,2,3,4,5,6,7,8,9]
def es_par(num):
	if(num%2==0):
		return True
#es lo mismo que hacerlo con esto
numeros_pares = filter(es_par, numeros)

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
```

# Ejercicio Práctico

```python
#ejercicio práctico de conocimientos hasta el momento:
# 1. Hoy faltó el profesor de clases y los alumnos decidieron armar su propia clase, uno de sus alumnas va a ser su profesor y otro va ser de asistente:
# a. Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
# b. El mayor es el profesor y el menor es el asistente, quien es quien?

def obtener_compañeros(cantidad):
	compañeros = []
	for i in range (7):
		nombre = input("Ingrese el nombre del compañero: ")
		edad = int(input("Ingrese la edad del compañero: "))
		compañero = [nombre, edad]
		compañeros.append(compañero)
	compañeros.sort(key=lambda x:x[1])
	asistente = compañeros[0][0]
	profesor = compañeros[-1][0]
	return asistente, profesor
asistente, profesor = obtener_compañeros(7)
print("El asistente es: ", asistente)
print("El profesor es: ", profesor)
```