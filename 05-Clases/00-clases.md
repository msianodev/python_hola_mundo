# Clases

## Definición de Clase

Las clases en Python son una forma de definir **objetos y sus comportamientos** en la programación orientada a objetos (OOP, por sus siglas en inglés). 

Una clase actúa como un molde para crear instancias de objetos. Dentro de una clase, puedes definir atributos (variables) y métodos (funciones) que determinan el estado y comportamiento del objeto.

```python
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2022)
mi_coche.mostrar_info()  # Esto imprimirá: Marca: Toyota, Modelo: Corolla, Año: 2022

```

En este ejemplo:

- `class Coche:` define una nueva clase llamada `Coche`.
- `__init__` es un método especial que se llama cuando se crea una nueva instancia de la clase. Se utiliza para inicializar los atributos del objeto.
- `mostrar_info` es un método que imprime la información del coche.

## Constructor

Un constructor en Python es un método especial que se llama automáticamente cuando se crea una nueva instancia de una clase. Su propósito principal es inicializar los atributos del objeto. En Python, el constructor se define mediante el método `__init__`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()  # Esto imprimirá: Hola, mi nombre es Juan y tengo 30 años.

```

En este ejemplo:

- `__init__` es el constructor de la clase `Persona`.
- El constructor toma dos parámetros adicionales (`nombre` y `edad`) y los asigna a los atributos del objeto (`self.nombre` y `self.edad`).

## Propiedades de Clase

Propiedad y atributo es lo mismo, siempre se refiere a las propiedades o atributos de una clase.

```python
class Perro:
	patas = 4 # Propiedad genérica de la clase
	
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad
	
	def habla(self):
		print(f"{self.nombre} dice: Guau!!")
		
		
Perro.patas = 3
mi_perro = Perro("Katrina", 1)
mi_perro.patas = 5

mi_perro2 = Perro("Milena", 2)
print(Perro.patas) # Output: 3
print(mi_perro.patas) # Output: 5

```

## Métodos de Clase

Los métodos de clase nos permiten definir métodos asociados a la clase y no al objeto que instanciemos. Se realiza de la siguiente manera:

```python
class Auto:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		
	# La propiedad de método de clase (Factory Method).
	@classmethod
	def factory(cls):
		return cls("Toyota","Corolla")

# Luego en el código main
auto1 = Auto("Mazda", "RX7")
auto2 = Auto("Nissan", "Sentra")
auto3 = Auto.factory()
print(auto3.marca, auto3.modelo) # Output: Toyota Corolla
```

Directamente creamos el objeto con sus valores desde la misma clase, no hay que olvidar el decorador de `@classmethod` que nos permite realizar dicha operación.

## Propiedades y métodos privados

Para evitar acceder a los métodos de una clase y nos cambien los valores es conveniente que los transformemos a privados.

```python
class Auto:
	def __init__(self, marca, modelo):
		self.__marca = marca
		self.__modelo = modelo
		
	# La propiedad de método de clase (Factory Method).
	@classmethod
	def factory(cls):
		return cls("Toyota","Corolla")
	
	# Utilizo un método para visualizar al propiedad
	def get_nombre(self):
		return(self.__nombre)
		
	# Podemos modificar las propiedades
	def set_nombre(self, nombre):
		self.__nombre = nombre

# Luego en el código main
auto1 = Auto("Mazda", "RX7")
auto2 = Auto("Nissan", "Sentra")
auto3 = Auto.factory()
print(auto3.marca, auto3.modelo) # Output: Toyota Corolla

print(auto1.get_nombre()) # Output: "Mazda RX7"

```

## Decorador Property

```python
class Perro:
	def __init__(self, nombre):
		self.nombre = nombre
		
	@property 
	# Le indica el método get_nombre() que lo transforma en una propiedad
	def nombre(self):
		return self.__nombre
	
	@nombre.setter
	def nombre(self, nombre):
		if nombre.strip(): # Quita los espacios en blanco
			self.__nombre = nombre
		return None
		
#	def set_nombre(self, nombre):
#		if nombre.strip(): # Quita los espacios en blanco
#			self.__nombre = nombre
#		return None
	
#	def get_nombre(self):
#		return self.__nombre

perro = Perro("Lila")
print(perro.nombre) # Output: Lila
```

con los decoradores de `property` y `@”metodo”.setter` queda exactamente como `get` y `set` pero de forma más convencional ocultando los accesos indebidos desde el intellisence de VScode.

## Métodos Mágicos

Los métodos mágicos con aquellos métodos que comienzan y terminan con `__` (doble guion bajo)

Los métodos mágicos en Python, también conocidos como "dunder methods" (abreviatura de "double underscore"), son métodos especiales que permiten definir el comportamiento de los objetos de una clase. Estos métodos se llaman automáticamente en determinadas situaciones, como cuando se realiza una operación matemática o se imprime un objeto. Los nombres de los métodos mágicos están rodeados por dos guiones bajos, por ejemplo, `__init__`, `__str__` y `__add__`.

Aquí te dejo algunos ejemplos comunes de métodos mágicos:

1. `__init__(self, ...)`: Este es el constructor de la clase y se llama cuando se crea una nueva instancia de la clase.
2. `__str__(self)`: Define la representación en cadena de un objeto, que es lo que se imprime cuando llamas a `print()` sobre una instancia de la clase.
3. `__repr__(self)`: Proporciona una representación oficial de la cadena del objeto, que debería ser clara y sin ambigüedades.
4. `__add__(self, other)`: Se utiliza para definir el comportamiento del operador `+` cuando se usa con instancias de la clase.
5. `__len__(self)`: Define el comportamiento de la función `len()` aplicada a instancias de la clase.

Los métodos mágicos son muy poderosos y permiten personalizar el comportamiento de los objetos de manera muy específica. Aquí tienes un ejemplo sencillo de una clase con algunos métodos mágicos:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

# Ejemplo de uso
p1 = Punto(2, 3)
p2 = Punto(4, 5)
p3 = p1 + p2
print(p3)  # Salida: (6, 8)

```

## Destructor

Un destructor en Python es un método mágico que se llama cuando un objeto está a punto de ser destruido. 

El método destructor se define usando `__del__(self)`. Su propósito principal es liberar recursos que el objeto pueda estar utilizando, como archivos abiertos o conexiones de red, justo antes de que el objeto sea eliminado de la memoria.

Es importante tener en cuenta que los destructores en Python no se utilizan con tanta frecuencia como en otros lenguajes de programación, porque Python cuenta con un recolector de basura (**garbage collector**) que maneja la memoria automáticamente. Sin embargo, los destructores pueden ser útiles en situaciones específicas donde necesitas asegurarte de que ciertos recursos se liberen adecuadamente.

Aquí tienes un ejemplo de una clase con un destructor:

```python
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo {nombre} abierto.")

    def __del__(self):
        self.archivo.close()
        print(f"Archivo {self.nombre} cerrado.")

# Ejemplo de uso
archivo = Archivo("mi_archivo.txt")
del archivo  # Esto llamará al destructor y cerrará el archivo

```

En este ejemplo, el destructor `__del__` cierra el archivo que fue abierto en el constructor `__init__`. Cuando el objeto `archivo` es eliminado con `del archivo`, el destructor se llama automáticamente y se cierra el archivo.

## Comparación de Objetos

Cuando instanciamos dos objetos con las mismas propiedades no significa que ambos objetos sean iguales. Cada instancia de una clase se guarda en una dirección de memoria distinta y por ende son variables totalmente diferentes. Para poder igualar una clase se debe realizar de la siguiente manera:

```python
class Coordenadas:
	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon
	
	# Debemos invocar al método
	def __eq__(self, otro):
		return self.lat == otro.lat and self.lon == otro.lon
		
	# Otro método es el de "not equal"
	def __ne__(self, otro):
		return self.lat != otro.lat or self.lon != otro.lon
		
	# Otro método es el de "menor que (<)"
	def __lt__(self, otro):
		self.lat < otro.lat
			
		
	coordenadas1 = Coordenadas(45, 12)
	coordenadas2 = Coordenadas(45, 12)
	
	print(coordenadas1 == coordenadas2) # Output: True (método __eq__)
	print(coordenadas1 != coordenadas2) # Output: False (método __ne__)
	print(coordenadas1 < coordenadas2) # Output: True (método __lt__)
```

## Contenedores

Son formas de insertar objetos dentro de otros objetos

```python
# Defino mi clase de Prodcuto con sus métodos correspondientes
class Producto:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio
		
	def __str__(self):
		return f"Producto: {self.nombre} - Precio: {self.precio}"
		
# Defino mi clase de Categoría con sus métodos correspondientes
class Categoria:
	productos = []
	def __init__(self, nombre, productos):
		self.nombre = nombre
		self.productos = productos
		
	def agregar_productos(self, producto):
		self.productos.append(producto)
		
	def imprimir(self):
		for producto in prodcutos:
			print(producto)
			

# Luego instanciamos los objetos y le aplicamos los métodos desarrollados
producto1 = Producto("Iphone", 1000)
producto2 = Producto("Macbook", 2000)
producto3 = Producto("SmartWatch",500)

lista_productos.append(producto1)
lista_productos.append(producto2)

categoria1 = Categoria("Apple", lista_productos)
categoria1.agregar_productos(producto3)
categoria1.imprimir()
# Output:
# Producto: Iphone - Precio: 1000
# Producto: Macbook - Precio: 2000
# Producto: SmartWatch - Precio: 500

```

## Herencia

La herencia es una de las características más potentes de la programación orientada a objetos (POO). En Python, la herencia permite crear una nueva clase (clase hija o subclase) basada en una clase existente (clase padre o superclase). 

La clase hija hereda todos los atributos y métodos de la clase padre, y además puede añadir nuevos atributos y métodos o modificar los heredados.

### **¿Para qué sirve la herencia?**

La herencia permite reutilizar código y evitar la redundancia. Si tienes una clase con atributos y métodos que también son útiles para otra clase, puedes crear una clase hija que herede de la primera y añadir o modificar lo que necesites. Esto hace que tu código sea más organizado, eficiente y fácil de mantener.

### **Ejemplo de herencia en Python**

Imagina que tienes una clase llamada `Animal` con los atributos `nombre` y `edad` y el método `comer()`. Ahora quieres crear una clase `Perro` que también tenga los atributos `nombre` y `edad` y el método `comer()`, pero además tenga el atributo `raza` y el método `ladrar()`. En lugar de volver a escribir todo el código de la clase `Animal`, puedes crear una clase `Perro` que herede de `Animal` y añadir los atributos y métodos específicos de los perros.

### **Código de ejemplo**

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("El animal está comiendo")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")

mi_perro = Perro("Max", 5, "Pastor Alemán")
print(mi_perro.nombre)  # Imprime "Max"
print(mi_perro.edad)    # Imprime 5
print(mi_perro.raza)   # Imprime "Pastor Alemán"
mi_perro.comer()       # Imprime "El animal está comiendo"
mi_perro.ladrar()      # Imprime "¡Guau!"

```

En este ejemplo, la clase `Perro` hereda de la clase `Animal`. El método `__init__()` de la clase `Perro` llama al método `__init__()` de la clase `Animal` usando `super().__init__(nombre, edad)` para inicializar los atributos `nombre` y `edad`. Luego, añade el atributo `raza` y el método `ladrar()`.

### **Tipos de herencia en Python**

Python admite varios tipos de herencia:

- **Herencia simple:** Una clase hija hereda de una sola clase padre.
- **Herencia múltiple:** Una clase hija hereda de varias clases padre.
- **Herencia multinivel:** Una clase hija hereda de una clase padre, que a su vez hereda de otra clase padre, y así sucesivamente.

**Ventajas de la herencia**

- **Reutilización de código:** Evita tener que escribir el mismo código varias veces.
- **Organización del código:** Permite agrupar clases relacionadas en una jerarquía.
- **Mantenibilidad del código:** Facilita la modificación y actualización del código.
- **Extensibilidad del código:** Permite añadir nuevas funcionalidades a clases existentes sin tener que modificarlas directamente.

## Herencia Multiple

La herencia múltiple en Python es un mecanismo que permite que una clase herede atributos y métodos de varias clases padre. Esto te da la flexibilidad de combinar funcionalidades de diferentes clases en una sola.

```python
class ClaseHija(ClasePadre1, ClasePadre2, ...):
    # Cuerpo de la clase hija

```

### **Orden de herencia (MRO - Method Resolution Order):**

El orden en que se listan las clases padre entre paréntesis define el orden en que se buscarán los atributos y métodos. Python utiliza un algoritmo llamado "C3 linearization" para determinar el MRO. En términos simples, el MRO prioriza la clase actual, luego busca en las clases padre de izquierda a derecha, y finalmente en las superclases de esas clases padre, siguiendo un orden de profundidad primero.

```python
class ClaseA:
    def metodo(self):
        print("Método de ClaseA")

class ClaseB:
    def metodo(self):
        print("Método de ClaseB")

class ClaseC(ClaseA, ClaseB):
    pass

mi_objeto = ClaseC()
mi_objeto.metodo()  # Imprime "Método de ClaseA"

```

En este ejemplo, `ClaseC` hereda de `ClaseA` y `ClaseB`. Como `ClaseA` se lista primero, su método `metodo()` se encuentra primero en el MRO y se ejecuta.

### **Ejemplo con super():**

```python
class ClaseA:
    def metodo(self):
        print("Método de ClaseA")

class ClaseB:
    def metodo(self):
        print("Método de ClaseB")

class ClaseC(ClaseA, ClaseB):
    def metodo(self):
        super().metodo()
        print("Método de ClaseC")

mi_objeto = ClaseC()
mi_objeto.metodo()  # Imprime "Método de ClaseA" y "Método de ClaseC"

```

En este caso, `super().metodo()` en `ClaseC` llama al método `metodo()` de la primera clase padre en el MRO (`ClaseA`).

**Consideraciones:**

- La herencia múltiple puede ser poderosa, pero también puede complicarse si no se usa con cuidado.
- Es importante entender el MRO para evitar comportamientos inesperados.
- Si varias clases padre tienen métodos con el mismo nombre, el método que se ejecute dependerá del MRO.

## Anulación de método

La anulación de métodos, también conocida como "method overriding", es un concepto  fundamental en la programación orientada a objetos (POO) que te permite modificar el comportamiento de un método heredado de una clase padre en una clase hija.

### **¿Por qué anular métodos?**

La anulación de métodos es útil cuando necesitas que una clase hija tenga un comportamiento diferente al de su clase padre para un método en particular. 

Por ejemplo, imagina que tienes una clase `Animal` con un método `hacer_sonido()`. Si tienes una clase `Perro` que hereda de `Animal`, puedes anular el método `hacer_sonido()` en la clase `Perro` para que ladre en lugar de hacer el sonido genérico de un animal.

### **¿Cómo funciona?**

Para anular un método, simplemente defines un método con el mismo nombre en la clase hija que el método que deseas anular en la clase padre. Cuando se llama a ese método en un objeto de la clase hija, se ejecutará la versión anulada del método en lugar de la versión original de la clase padre.

```python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de animal")

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

mi_perro = Perro()
mi_perro.hacer_sonido()  # Imprime "¡Guau!"

```

En este ejemplo, la clase `Perro` anula el método `hacer_sonido()` de la clase `Animal`. Cuando se llama a `hacer_sonido()` en el objeto `mi_perro` (que es una instancia de `Perro`), se ejecuta la versión anulada del método, que imprime "¡Guau!".

### **Llamar al método original:**

Si necesitas acceder a la versión original del método en la clase padre desde la clase hija, puedes usar la función `super()`:

```python
class Perro(Animal):
    def hacer_sonido(self):
        super().hacer_sonido()  # Llama al método original de la clase Animal
        print("¡Guau!")

```

En este caso, `mi_perro.hacer_sonido()` imprimirá primero "Sonido genérico de animal" (debido a la llamada a `super()`) y luego "¡Guau!".

**Puntos importantes:**

- La anulación de métodos te permite personalizar el comportamiento de las clases hijas sin tener que modificar el código de las clases padre.
- La anulación de métodos es un concepto clave en la POO que fomenta la reutilización del código y la flexibilidad en el diseño de tus clases.

# Ejemplo Real

Crearemos una clase que implemente los métodos de un CRUD

```python
class Model():
	tabla = False
	def __init__(self):
		if not self.tabla:
			print("Error, tienes que definir una tabla")
			
	def guardar(self):
		print(f"Guardando {self.tabla} en BBDD")
	
	@classmethod
	def buscar_por_id(self, _id):
		print(f"buscando por ID: {_id} en la tabla {self.tabla}")

class Usuario(Model):
	tabla = "Usuario"
	
# En nuestro Main
usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
```

## Clases Abstractas

Las clases abstractas son un concepto importante en la Programación Orientada a Objetos (POO). 

### Clases Abstractas en POO

Una clase abstracta es una clase que no se puede instanciar directamente y está pensada para ser heredada por otras clases. Sirve como una plantilla y puede contener métodos abstractos (métodos sin implementación) que deben ser implementados por las clases derivadas.

### Uso de Clases Abstractas en Python

En Python, para definir una clase abstracta, usamos el módulo `abc` (Abstract Base Classes). Aquí tienes los pasos a seguir:

1. **Importar el Módulo `abc`:**
    
    ```python
    from abc import ABC, abstractmethod
    
    ```
    
2. **Definir la Clase Abstracta:**
    
    ```python
    class Animal(ABC):
        @abstractmethod
        def hacer_sonido(self):
            pass
    
    ```
    
3. **Implementar Clases Derivadas:**
    
    ```python
    class Perro(Animal):
        def hacer_sonido(self):
            return "Guau!"
    
    class Gato(Animal):
        def hacer_sonido(self):
            return "Miau!"
    
    ```
    
4. **Crear Instancias de las Clases Derivadas:**
    
    ```python
    perro = Perro()
    gato = Gato()
    
    print(perro.hacer_sonido())  # Output: Guau!
    print(gato.hacer_sonido())   # Output: Miau!
    
    ```
    

En resumen:

- Importas el módulo `abc`.
- Defines una clase abstracta heredando de `ABC`.
- Declaras métodos abstractos con el decorador `@abstractmethod`.
- Implementas las clases derivadas proporcionando la implementación de los métodos abstractos.

---

El decorador `@abstractmethod` es esencial para declarar métodos abstractos en clases abstractas. También mencionaste `@property`, que es otro decorador útil en Python, aunque no es específico para clases abstractas.

### Decorador `@abstractmethod`

El decorador `@abstractmethod` se utiliza para definir métodos que deben ser implementados por cualquier subclase concreta. Aquí tienes un ejemplo:

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)

# No puedes instanciar Figura directamente porque tiene métodos abstractos
circulo = Circulo(5)
print(circulo.area())  # Output: 78.5

```

### Decorador `@property`

El decorador `@property` se utiliza para definir métodos que pueden ser accedidos como atributos. Es particularmente útil para encapsular datos y añadir lógica adicional cuando se obtiene o establece el valor de un atributo.

### Uso de `@property`

```python
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor:
            self._nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío")

persona = Persona("Juan")
print(persona.nombre)  # Output: Juan

persona.nombre = "Carlos"
print(persona.nombre)  # Output: Carlos

```

### Casos de Uso

- Usa `@abstractmethod` cuando quieras asegurarte de que cualquier subclase concreta implemente un método específico.
- Usa `@property` cuando necesites controlar el acceso y modificación de atributos en tus objetos, proporcionando un interfaz de acceso como si fueran atributos, pero con la capacidad de añadir lógica adicional.

# Polimorfismo

El polimorfismo es un concepto fundamental en la Programación Orientada a Objetos (POO) que permite a las clases derivadas compartir la misma interfaz para diferentes tipos de datos o comportamientos, asegurando que se puedan usar de manera intercambiable. En otras palabras, el polimorfismo permite que el mismo método se comporte de diferentes maneras según el objeto que lo invoque.

### Ejemplo Básico de Polimorfismo en Python

Te mostraré un ejemplo sencillo utilizando Python:

```python
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

def emitir_sonido(animal):
    print(animal.hacer_sonido())

# Polimorfismo en acción
perro = Perro()
gato = Gato()

emitir_sonido(perro)  # Output: Guau!
emitir_sonido(gato)   # Output: Miau!

```

En este ejemplo:

1. Tenemos una clase base `Animal` con un método `hacer_sonido` que no tiene implementación.
2. Las clases `Perro` y `Gato` heredan de `Animal` y cada una implementa el método `hacer_sonido` de manera diferente.
3. La función `emitir_sonido` recibe un objeto de tipo `Animal` y llama al método `hacer_sonido`, demostrando el polimorfismo al funcionar correctamente con diferentes tipos de animales (`Perro` y `Gato`).

El polimorfismo te permite escribir código más flexible y reutilizable, ya que puedes trabajar con clases derivadas sin preocuparte por sus diferencias internas. 😊

# **Duck Typing en Python**

El [duck typing](https://docs.python.org/3/glossary.html#term-duck-typing) o tipado de pato es un concepto relacionado con la programación que aplica a ciertos lenguajes [orientados a objetos](https://ellibrodepython.com/programacion-orientada-a-objetos-python), y que tiene origen en la siguiente frase:

> If it walks like a duck and it quacks like a duck, then it must be a duck
> 

Lo que se podría traducir al español como. **Si camina como un pato y habla como un pato, entonces tiene que ser un pato**.

¿Y qué relación tienen los patos con la programación? Pues bien, se trata de un símil en el que los **patos son objetos** y **hablar/andar métodos**. Es decir, que si un determinado objeto tiene los métodos que nos interesan, nos basta, siendo su tipo irrelevante.

Dicho de otra manera, no mires si es un pato. Fíjate si habla como un pato, camina como un pato, etc. Si cumple con todas estas características, ¿no podríamos acaso decir que se trata de un pato?

> Don’t check whether it is-a duck: check whether it quacks-like-a duck, walks-like-a duck, etc, etc, depending on exactly what subset of duck-like behavior you need to play your language-games with. (comp.lang.python, Jul. 26, 2000) — Alex Martelli
> 

El concepto de *duck typing* se fundamenta en el [razonamiento inductivo](https://es.wikipedia.org/wiki/Razonamiento_inductivo), donde una serie de premisas apoyan la conclusión, pero no la garantizan. Si vemos a un animal que parece un pato, habla como tal y anda como tal, sería razonable pensar que se trata de un pato, pero sin un test de ADN nunca estaríamos al cien por cien seguros.

Una vez entendido el origen del concepto, veamos lo que realmente significa esto en Python. En pocas palabras, **a Python le dan igual los tipos de los objetos, lo único que le importan son los métodos**.

Definamos una clase `Pato` con un método `hablar()`.

```python
class Pato:
    def hablar(self):
        print("¡Cua!, Cua!")
```

Y llamamos al método de la siguiente forma.

```python
p = Pato()
p.hablar()
# ¡Cua!, Cua!
```

Hasta aquí nada nuevo, pero vamos a definir una función `llama_hablar()`, que llama al método `hablar()` del objeto que se le pase.

```python
def llama_hablar(x):
    x.hablar()
```

Como puedes observar, en Python **no es necesario especificar los tipos**, simplemente decimos que el parámetro de entrada tiene el nombre `x`, pero no especificamos su tipo.

Cuando Python entra en la función y evalúa `x.hablar()`, le da igual el tipo al que pertenezca `x` siempre y cuando tenga el método `hablar()`. Esto es el *duck typing* en todo su esplendor.

```python
p = Pato()
llama_hablar(p)
# ¡Cua!, Cua!
```

¿Y qué pasa si usamos otros objetos que no son de la clase `Pato`? Pues bien, como hemos dicho, a la función `llama_hablar()` le da igual el tipo. Lo único que el importa es que el objeto tenga el método `hablar()`.

Definamos tres clases de animales distintas que implementan el método `hablar()`. Nótese que no existe [herencia](https://ellibrodepython.com/herencia-en-python) entre ellas, son clases totalmente independientes. De haberla estaríamos hablando de [polimorfismo](https://ellibrodepython.com/polimorfismo-en-programacion).

```python
class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")
```

Y como es de esperar la función `llama_hablar()` funciona correctamente con todos los objetos.

```python
llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!
```

Otra forma de verlo, es iterando una lista con diferentes animales, donde `animal` va tomando los valores de cada objeto animal. Todo un ejemplo del *duck typing* y del tipado dinámico en Python.

```python
lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!
```

#