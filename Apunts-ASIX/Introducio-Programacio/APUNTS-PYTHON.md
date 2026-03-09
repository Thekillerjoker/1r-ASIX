# Para Hacer comandos de shel a python se usa el modulo import os.
*Esto sirve para que tu al ejecutar el codigo en un sistema operativo te cargue solo el codigo que este dentro de la libreria de import os, y asi no tenga que cargar todo el codigo*
```python
import os
os.system('ls -l')

```
## Para hacerlo con guardando a salida:
```python
import os
stream = os.popen('ls -l')
sortida = stream.read()
print("sortida", sortida)
```

# Variables amb diferents valors
**Array:para guardar varios valores en un amisma variable pero no son para python por eso se utilizan Listas que es lo mismo pero de python.**
```python
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# Tambien asu
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
# Array En la programacion contamos dessde el 0
cars = ["Ford", "Volvo", "BMW"]
x = cars[2]
print(cars[0])
## 0,1,2 SON LAS POSICIONES: 0 es la primera "Ford", 1 es "Volvo", y 2 es "bmw".
cars = ["Ford", "Volvo", "BMW"]

print(cars[0]) #Mostrara Ford.
print(cars[1]) #MosreE Volvo.
print(cars[2]) #mostrara BMW
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
#Esto te muestra el valor de cars, y al poner cars[0] = "Toyota" cambias el valor de la posicion 0 por Toyota por lo tanto te mostrara "Toyota", "Volvo", "BMW". 
cars = ["Ford", "Volvo", "BMW", "Subaru", "Tesla", "Lamborguini", "Xiamoi", "Maseratti", "Seat"]
x = len(cars)
print(x)
#Imprimira la longitud de valores de la variable. Y mostrara 9 aunque haya 8 valores porque cuenta desde el 0 porque si pones 8 no son todos los valores porque hay nueve y como cuenta desde el 0 hay ocho pero claro con ocho Seat no lo cuenta.
```
## Recorregut vs Cerca:
**Recorregut:** *Quantes persones porten bambes del decattlon, me he tenido que mirar todos uno por uno*
**Cerca:** *Quina marca es l'ordinado de l'asia nomes vas a mirar aquell valor .*
### Recorregut:

### Cerca:

```python
numeros = [1, 2, 3]
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1
# te mostrara 1, 2, 3  porque mientras i sea mas pequeño que la length es decir 3 muestra el numero que esta en el valor i que es 0 y com i += 1 pues hace el valor y le suma 1.add()
```
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 33, -9, 0, 44]
numero_cercat = 4

i = 0
trobat = False

while not trobat and i < len(numeros):
trobat = (numeros[i] == numero_cercat)
i += 1

if trobat:
print(f"{numero_cercat} trobat a la posició {i - 1}")
else:
print(f"{numero_cercat} no trobat")
# el bucle te dice mientras no encuentres el numero buscado y sea mas pequeño que la longitud , entonces con trobat = (numeros[i] == numero_cercat) lo que te hace es si i que es cero es el mismo numero que valor_cercat, no entonces lo que haces es incrementar el valro de i en 1 entomces 0+1 es 1 entonces te salta al siguiente valor y vuelve a mirar 1 es igual al numero buscado, no entonces increment sigue buscando una vez lo encurentre, es decir i es igual a el numero i =4 es 4 entonces sale del bule y con el if te da la posicion y como he ido incrementando el valor de i en uno por eso le resto -1 porque sino te meiraria desde la posicion 1, y al poner -1 te cuenta desde la possicion 0 y te doce la posicion en la que esta el valor,  y si acaba todos los valores y no lo encuentra pues muestra no lo he encontrado.
#la i te indica pues controla los numeros que voy buscando.
# con el trobat es false porque es false  entocnes con el while not trobat dices mientras trobat no sea true porque cuando encuentre el trobat encuentre el numero que lo hemos indicado con el trobtat = (numeros[i] == numero_cercat) pues entonces conbierte el trobat en true.

```
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 33, -9, 0, 44]

i = 0
while i < len(numeros):
print(numeros[i])
# Entonces esto te hace lo mismo mientras i sea mas pequeño que la longitud total de numeros printea.
```
## Diccionari:
**Els diccionaris s'utilitzen per emmagatzemar valors de dades en els parells de valors clau.**

**Un diccionari és una col·lecció ordenada*, variable i no Permet duplicar els duplicats.**

*Com un array pero s'escriuen amb claus { i tenen claus i valors*
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
*Aixo imprimira cada valor de la seguent manera: 'nom_clau': 'Valor'*

**Articles del diccionari**

*Els elements del diccionari s'ordenen, es poden canviar i no permeten duplicats.*

*Els elements del diccionari es presenten en els parells de valors clau, i es poden fer referència a utilitzant el nom de la clau.*
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
*Aixo imprimeix el valor de brand que es Ford.*

**Ordenat o desordenat?**

*Quan diem que s'ordenen diccionaris, vol dir que els elements tenen un ordre definit, i que l'ordre no canviarà.*

*Desordenat significa que els elements no tenir un ordre definit, no es pot referir a un element mitjançant l'ús d'un índex*

**Canviable**

*Els diccionaris són canviables, el que significa que podem canviar, afegir o eliminar elements després de l'element S'ha creat el diccionari*
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```

*Aixo imprimeix {'brand': 'Ford', 'model': 'Mustang', 'year': 2020} i no imprimeix el year 1964 ja que no permet duplicats per tant mostra el ultim valor ja que python es un llenguatje variable*
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
```

*Aixo mostra 3*
*Imprimeix el nombre d'elements del diccionari:*

**Articles del diccionari - Tipus de dades**

*Els valors en els elements del diccionari poden ser de qualsevol tipus de dades:*

```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
```
*Aixo imprimeix {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}.*

**tipus()**

*Des de la perspectiva de Python, els diccionaris es defineixen com a objectes amb el tipus de dades 'dict':*

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```
*Aixo imprimeix el tipus de dades d'un diccionari és ha dir axio imprimira :<class 'dict'> .*

**The dict() Constructor /El dictat() Constructor:**

*També és possible utilitzar el constructor de dict) per fer un diccionari.*

*Utilitzant el mètode dict() per fer un diccionari:*
```python
thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict) 
```
*aixo imprimira : {'name': 'John', 'age': 36, 'country': 'Norway'}.*

**Accés a articles:**

*Podeu accedir als elements d'un diccionari referint-vos al seu nom clau, a l'interior claudàtors:*

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
```
*Aixo mostrara Mustang.*
## Python Dictionaris:
![Infografia-Python-Dictionari](./infografia-python-diccionaris.png)
## Python Collections:
![Infografia-Python-Collections](./infografia-python-collections.png)

*com mostrar el diccionari en Python tal i com demana el primer exercici?:*
```python
diccionari = dict()


#...


elements = [f"{nom}={data}" for nom, data in diccionari.items()]
sortida = "{" + ", ".join(elements) + "}"
print(sortida)

```
# Fitchers:

## Exceptions (Errors):
*Quan hi ha un error les excepcions es per cuan salti un error mostrar un misatje personalitzat*


**Exempe**
```python
print(x)
#Com que no hi ha la variable x 
```
