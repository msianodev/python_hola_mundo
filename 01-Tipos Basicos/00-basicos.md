# Métodos Principales

# Métodos de cadenas (String Methods)

**`print()`**: Muestra información en la consola.

```python
print("Hola, mundo!")
```

`dir**()**`: se utiliza para obtener una lista de nombres en el espacio de nombres actual o de un objeto en particular. Puedes usarlo sin argumentos para obtener los nombres en el espacio de nombres actual o con un objeto como argumento para obtener los atributos y métodos disponibles para ese objeto.

```python
#sin argumentos
nombres = dir()
print(nombres)

#con argumentos
lista = [1, 2, 3]
atributos_metodos = dir(lista)
print(atributos_metodos)
```

Esto devolverá una lista de atributos y métodos disponibles para el objeto **`lista`**. Estos pueden incluir métodos como **`append()`**, **`extend()`**, **`count()`**, entre otros, así como atributos específicos del objeto.

**`upper()`**: Este método convierte todos los caracteres de una cadena a mayúsculas.

```python
texto = "Hola, mundo!"
texto_mayusculas = texto.upper()
print(texto_mayusculas)
```

**`lower()`**: Este método convierte todos los caracteres de una cadena a minúsculas.

```python
texto = "Hola, mundo!"
texto_minusculas = texto.lower()
print(texto_minusculas)
```

**`capitalize()`**: Este método convierte el primer carácter de una cadena a mayúscula y el resto a minúsculas.

```python
texto = "hola, mundo!"
texto_capitalizado = texto.capitalize()
print(texto_capitalizado)
```

**`find(subcadena[, inicio[, fin]])`**:

- Busca la subcadena dentro de la cadena y devuelve la posición de la primera ocurrencia.
- Si no encuentra la subcadena, devuelve -1.
- Puedes proporcionar argumentos opcionales **`inicio`** y **`fin`** para especificar un rango de búsqueda.

```python
frase = "Hola, mundo!"
posicion = frase.find("mundo")
print(posicion)  # Devolverá la posición de "mundo" en la cadena.
```

**`index(subcadena[, inicio[, fin]])`**:

- Similar a **`find()`**, busca la subcadena dentro de la cadena y devuelve la posición de la primera ocurrencia.
- Sin embargo, si no encuentra la subcadena, en lugar de devolver -1, genera una excepción (**`ValueError`**).
- También acepta argumentos opcionales **`inicio`** y **`fin`** para especificar un rango de búsqueda.

```python
frase = "Hola, mundo!"
posicion = frase.index("mundo")
print(posicion)  # Devolverá la posición de "mundo" en la cadena.
```

**`isnumeric()`**:

- Devuelve **`True`** si todos los caracteres de la cadena son numéricos (0-9), de lo contrario, devuelve **`False`**.
- Espacios en blanco y otros caracteres no numéricos harán que este método devuelva **`False`**.

```python
cadena_numerica = "12345"
resultado = cadena_numerica.isnumeric()
print(resultado)  # Devolverá True
```

```python
cadena_no_numerica = "12.34"
resultado_no_numerico = cadena_no_numerica.isnumeric()
print(resultado_no_numerico)  # Devolverá False
```

**`isalpha()`**:

- Devuelve **`True`** si todos los caracteres de la cadena son caracteres alfabéticos (letras), de lo contrario, devuelve **`False`**.
- Espacios en blanco y otros caracteres no alfabéticos harán que este método devuelva **`False`**.

```python
cadena_alfabetica = "abc"
resultado_alfabetico = cadena_alfabetica.isalpha()
print(resultado_alfabetico)  # Devolverá True
```

```python
cadena_no_alfabetica = "abc123"
resultado_no_alfabetico = cadena_no_alfabetica.isalpha()
print(resultado_no_alfabetico)  # Devolverá False
```

**`count(subcadena)`**:

- Devuelve el número de veces que aparece la subcadena dentro de la cadena principal.
- Puede incluir argumentos opcionales **`inicio`** y **`fin`** para especificar un rango de búsqueda.

```python
frase = "Hola, hola, mundo!"
cantidad = frase.count("hola")
print(cantidad)  # Devolverá el número de veces que "hola" aparece en la cadena.
```

**`len(cadena)`**:

- Devuelve la longitud (número de caracteres) de la cadena.
- Puede aplicarse a cualquier secuencia en Python, no solo a cadenas.

```python
frase = "Hola, mundo!"
longitud = len(frase)
print(longitud)  # Devolverá la longitud de la cadena.
```

**`endswith(subcadena[, inicio[, fin]])`**:

- Devuelve **`True`** si la cadena termina con la subcadena especificada, de lo contrario, devuelve **`False`**.
- Puedes proporcionar argumentos opcionales **`inicio`** y **`fin`** para especificar un rango de búsqueda.

```python
cadena = "Hola, mundo!"
resultado = cadena.endswith("mundo!")
print(resultado)  # Devolverá True
```

**`startswith(subcadena[, inicio[, fin]])`**:

- Devuelve **`True`** si la cadena comienza con la subcadena especificada, de lo contrario, devuelve **`False`**.
- También acepta argumentos opcionales **`inicio`** y **`fin`** para especificar un rango de búsqueda.

```python
cadena = "Hola, mundo!"
resultado = cadena.startswith("Hola")
print(resultado)  # Devolverá True
```

**`replace(viejo, nuevo[, cantidad])`**:

- Este método reemplaza todas las ocurrencias de la subcadena **`viejo`** con la subcadena **`nuevo`** en una cadena.
- Opcionalmente, puedes proporcionar el argumento **`cantidad`** para especificar cuántas ocurrencias deben ser reemplazadas.

```python
frase = "Hola, mundo!"
nueva_frase = frase.replace("mundo", "python")
print(nueva_frase)
```

**`split()`** : separa cadenas con la cadena que le pasemos

```python
frase = "Hola, mundo!"
palabras = frase.split()
print(palabras) #output: ['Hola', 'mundo']
```

 **`strip()`** : sirve para eliminar los caracteres especificados (o espacios en blanco por defecto) al principio y al final de una cadena.

```python
texto = "   Hola, mundo!   "
print(texto.strip())
#Hola, mundo!

```

```python
texto = "xxxHola, mundoxxx"
print(texto.strip("x"))
# Hola, mundo

```

# Métodos de listas

Métodos para aplicar a listas para poder operarlas

1. `list()`: Crea una nueva lista o convierte un iterable en una lista.
    
    ```python
    # Crear una lista vacía
    lista_vacia = list()
    print(lista_vacia)  # Output: []
    
    # Convertir una cadena en una lista de caracteres
    cadena = "Hola"
    lista_de_caracteres = list(cadena)
    print(lista_de_caracteres)  # Output: ['H', 'o', 'l', 'a']
    ```
    
2. `len()`: Devuelve la longitud (número de elementos) de una lista.
    
    ```python
    mi_lista = [1, 2, 3, 4, 5]
    longitud = len(mi_lista)
    print(longitud)  # Output: 5
    ```
    
3. `append()`: Agrega un elemento al final de la lista.
    
    ```python
    frutas = ["manzana", "banana", "uva"]
    frutas.append("pera")
    print(frutas)  # Output: ['manzana', 'banana', 'uva', 'pera']
    ```
    
4. `insert()`: Inserta un elemento en una posición específica de la lista.
    
    ```python
    numeros = [1, 2, 3, 4]
    numeros.insert(2, 99)
    print(numeros)  # Output: [1, 2, 99, 3, 4]
    ```
    
5. `extend()`: Extiende la lista agregando elementos de otro iterable.
    
    ```python
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista1.extend(lista2)
    print(lista1)  # Output: [1, 2, 3, 4, 5, 6]
    ```
    
6. `pop()`: Elimina y devuelve el elemento en una posición específica de la lista.
    
    ```python
    colores = ["rojo", "verde", "azul"]
    color_eliminado = colores.pop(1)
    print(colores)  # Output: ['rojo', 'azul']
    print(color_eliminado)  # Output: verde
    #si ponemos pop(-1) elimina el último o (-2) para el anteúltimo y así sucesivamente
    ```
    
7. `remove()`: Elimina la primera ocurrencia del valor especificado.
    
    ```python
    numeros = [1, 2, 3, 4, 3]
    numeros.remove(3)
    print(numeros)  # Output: [1, 2, 4, 3]
    ```
    
8. `clear()`: Elimina todos los elementos de la lista.
    
    ```python
    mi_lista = [1, 2, 3, 4, 5]
    mi_lista.clear()
    print(mi_lista)  # Output: []
    ```
    
9. `sort()`: Ordena los elementos de la lista en su lugar.
    
    ```python
    numeros = [4, 2, 1, 3]
    numeros.sort()
    print(numeros)  # Output: [1, 2, 3, 4]
    ```
    
10. `reverse()`: Invierte el orden de los elementos de la lista.
    
    ```python
    letras = ['a', 'b', 'c']
    letras.reverse()
    print(letras)  # Output: ['c', 'b', 'a']
    ```
    

# Métodos de diccionarios

1. `keys()`: Devuelve una vista de todas las claves en el diccionario.
    
    ```python
    mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
    claves = mi_diccionario.keys()
    print(claves)  # Output: dict_keys(['a', 'b', 'c'])
    ```
    
2. `get()`: Devuelve el valor asociado a una clave, o un valor predeterminado si la clave no está en el diccionario.
    
    ```python
    mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
    valor = mi_diccionario.get('b', 'No encontrado')
    print(valor)  # Output: 2
    
    valor_no_existente = mi_diccionario.get('z', 'No encontrado')
    print(valor_no_existente)  # Output: No encontrado
    ```
    
3. `clear()`: Elimina todos los elementos del diccionario.
    
    ```python
    mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
    mi_diccionario.clear()
    print(mi_diccionario)  # Output: {}
    ```
    
4. `pop()`: Elimina y devuelve el valor asociado a una clave específica.
    
    ```python
    mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
    valor_eliminado = mi_diccionario.pop('b')
    print(mi_diccionario)  # Output: {'a': 1, 'c': 3}
    print(valor_eliminado)  # Output: 2
    ```
    
5. `items()`: Devuelve una vista de tuplas que contienen pares (clave, valor) del diccionario.
    
    ```python
    mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
    elementos = mi_diccionario.items()
    print(elementos)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
    ```
    

# Entrada de datos (inputs)

`input()`: Permite el ingreso de datos por teclado en la consola.

```python
nombre = input("Ingrese su nombre: ")
print(f"Hola", nombre) 
#Output: Ingrese su nombre:
#Output: Hola (lo que ingresemos)

numero = input("Ingrese un numero: ")
resultado = int(numero) + 10
print(f"El resultado es: {resultado}")
#Output: Ingrese un numero:
#Output: El resultado es (lo que ingresemos)+10
```