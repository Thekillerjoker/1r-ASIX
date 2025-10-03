# Conceptos basicos del Python
*Cuando se utilizan las dobles comillas estamos creando una cadena de texto.*
**Print**:
*Print sirve para mostrar un mensaje en la consola por ejemplo:*
```python
print("¡Hola Mundo!")
```
*Formas de ejecutar Un Python desde la termianl python3 o desde el debuger*
>[!TIP]- Tip
En pyhton las cadenas de texto también se puden hacer utilizando solo una comilla.
print(¡'Esto también funciona!)
Cuando utilizar una comilla o dos
dependinedo del caso es decir si tu dentro de una cadena de texto quieres poner mas texto entre comillas 
print('¡Esto también "Funciona" con una comilla!')
>
## Imprimir varios valores con Print:
*Para imprimir variso valores se ha de hacer poniendo comas.*
```python
print("Python", "es", "genial")
```
*Para personalizar el separador por defecto es con el modulo sep*
```python
print("Python", "es", "Brutal", sep ="-")
```
*Para hcerlo en una linea con el comando end*
```python
print("Esto se imprime", end = " ")
print("en una línea")
```
-----
# 2. Types
*Pyton tiene Varios tiupos de datos:*
*int, float, complex, str, bool, NoneType, list, tuple, dict, range,set*
1. **Nombres enteros:**
*Para nombres enteros utilizamos el valor int y se hace de la siguiente manera:*
```python
print("int:")
print(10)
print(0)
print(-5)
#También puede haber muchos numeros siempre que sean enteros
print(1245567980044356)
```
*Para saber si un numero que tipo de valor tiene se utiliza la funcion type que funciona de la siguiente manera:*
"con print(type(10)) le estamos indicando imprime cual es el tipo del valor 10."
*Esto lo que te imprimira al ejecutarlo es <class 'int'> que lo que te esta diciendo que el valor 10 es un valor de tipo int es decir entero.*

"""
En python asi puedes ahcer una cadena de texto que si no lo asignas a nada se detecta como un comentario.
"""
2. **Numeros decimales:**
*Para numeros decimales se utiliza float si utilizas notacion ceientifica tambien es decimal.*

```python
print("float:")
print(10.14)
print(1.0)
print(1e3)
```
3. **Numeros complejos**
*Para los numeros complejos se utiliza complex, es para mezcla de un numero real y uno que no conoces por ejemplo un numero científico:*
```python
print("complex:")
print(1+2j)
print(type(1+2j))
```
4. **Cadenas de texto**
*Para cadenas de texto se utiliza string (str)*
*Es lo que ya hemos visto lo que va entre comillas y todo lo que va entre comillas es cadena de texto incluso sin son numeros*
>[!IMPORTANT]- Explicacion
>si pongo print(10) es un numero si pongo print("10") el diez es texto por lo cual no se puede sumar.
>
5. **Los boleanos**
*Los boleanos son el true y el false y si haces comparaciones tambien es boleano por ejemlo si pones 1<2.*

6. **La ausencia de valor**
*Con el NonType es el valor que significa la ausencia de valor.*
```python
print(type(None))
```
------
# 3. Casting de Tipos:
**Tranformar un tipo de valor a otro**

1. **Conversión de tipos:**
*Por ejemplo cambiar una cadena de texto a un numero entero.*
```python
print(type(int("100")))
#O por ejemplo si tengo un print(2+" 100") no me va ha dejar
print(2 + int("100"))
#O
print("100" + str(2))
#lo que hace no es sumar sino juntar las dos cadenas de texto
```
*Para numeros boleanos*
```python
print(bool(3))#seria true
print(bool(0))#seria false
print(bool(-1))#Seria true ya que el unico que se transforma en negativo es decir false es el o o si esta vacio por ejemlpo:
print(bool(""))#Es fasle esta vacio
print(bool(" "))#Es true
print(bool("False"))#Es true
```
-------------------------
# 4. Variables:
**Las variables sirven para guardar datos en memoria.**
*Es decir guardan datos en memorias le dan un nombre y asi podernso referir a ellos cuando queramos y como queramos.*
>[!IMPORTANT]- Assignar una variable.
>Para asignar una variable solo necesitas poner el =
>my_name = "Sergi"
>print(my_name)
>Te muestra Sergi
>
>[!IMPORTANT]- python es de tipado dinámico:
> Es decir el tipo de dato se determina en tiempo de ejecución.
> Es decir que  no tienes que declararlo explícitamente.
>

>[!TIP]-Ejemplos:
>name = "Sergi" ya nos indica que es de tipo str.
>print(type(name)) ya nos mostrara que es tipo str.
> y es cambiante en el tiempo es decir si añado :
> name = 32
> print(type(name))
> Me va ha decir que priemro el valor name era str y ahora es int.
>

>[!IMPORTANT]- Python no cambia el formato de tipos automaticos.
> Es decir que si pones print(10 + "2") no te lo va ha cambiar y va ha petar.
> Ahora que quieres cambiar el formato de algo estatico es con las fstrings que es con f.
>
-------------
**Ejemplo de Fstring:**
```python
my_name = "Sergi"
age = 21
print(f"Hola me llamo {my_name} y tengo {age} años")
#Esto te mostrara hola me llamo Sergi y tengi 21 años
```
>[!TIP]
>Tambien se pueden hacer sumas dentro de una variable.
>
```python
my_name = "Sergi"
age = 21
print(f"Hola me llamo {my_name} y tengo {age + 3} años")
#Esto me daria hola me llamo Sergi y tengo 23 años
```
2. **Convecniones de nombres de variables:**
- *Formas correctas:*
mi_nombre_variable = "ok"
nombre = "Ok"
mi_nombre_de_variable_123 = "Ok"

- *Formas no correctas:*
MiNombreDeVariable = "No" 
minombrevariable = "No"
123_variable = "NO"
Mi-Variable = "No"

>[!TIP]- Constantes 
>Utilizar las mayusculas para las constantes, es decir utilizar los nombre todo en mayusculas para una variable que no valor que no vayas a cambiar.
>
>[!IMPORTANT]-Valores reservados
>No puedes assignar como nombre de una variable un nombre reservado de python.
>Es decir aquellos nombres que Python tiene reservados para funcionar.
>
**Nombres reservados de Python:**
*True, False, None, and, as, assert, async,await,break,class,continue*
*def,del,elif,else,except,finally,for,from,global,if,import,in,is,lambda,nonlocal,not*
*or,pass,raise,return,try,while,with,yield*
```python
is_user_logged_in: bool = true
print(is_user_logged_in)
is_user_logged_in = 42
print(is_user_logged_in)
```
-----------------
# 5. Funcion Input:
*La función input te permite pedir información al usuario para poderlso utilizar.*

1. **Ejmplo para pedir un nombre:**
```python
print("Hola ¿cómo te llamas?")
nombre = input()
print(f"Hola {nombre}, encantado de conocerte")
```
>[!TIP]- Formato mas rápido.
>El input puede ir dentro de la misma variable.
>
```python
nombre = input("Hola ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")
```
*Para pedir informacion que es numerico ya que la infromación que obtenga de input siempre sera de tipo cadena de texto*
```python
age = input("¿Cúantos años tienes?\n")
age= int(age)
print(f"Tienes {age} años")
```
2. **Obtener multiples valores a la vez**
```python
country, city = input("¿En qué país y ciudad vives?\n").split()
print(f"vives en {country}, {city}")
```

*Para obtener multiples valores a la vez se utiliza .split*
*Con split hacemos que el contenido que esta dentro de el input la vamos a separar y el primer elemento va ha permanecer a la variable country, y el segundo a la variable city, es decir que en que "país" va a permanecer a "country" y "ciudad" va a permanecer a "city"*
>[!IMPORTANT]- Formato de las Respuestas.
> Split coje la información en espacios por lo que cuando el usuario ha de escribir la informacion lo ha de separar con espacio por ejemplo:
> ¿En que país y ciudad vives?
> España Figueres.
>
# 6. Sentencias Condicionales:
**Condicionales (if, elif, else):**
*Permiten ejecutar bloques de código si se cumplen ciertas condiciones.*
1. **IF**
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
```
>[!TIP]Tip de los bloques
>El if funciona que todo lo que es bloque de codigo de la condicional ha de estar separado por un tabulador, entonces todo lo que quieres que se ejecute o en este caso por ejemplo se imprima solo si se cumple esa condicion ha de estar dentro del if es decir con un tabulador.
>
- **Demostracion como funcionaria el if:**
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
#Esto se imprimiria eres mayor de edad ya que se cumple la condicion
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
# No se imprimiria ya que la condicion no se cumple ya que ahora edad es = 15
```
2. **El else:**
*El else funciona para decir y si no se cumple entonces pasa esto.*
```python
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```
>[!IMPORTANT]- Evitar usar el else.
> Evitar poner else ya que lo que haces es hacer una bifurcación es decir que tu codigó tenga dos posibilidades.
> Cuantas mas bifurcaciones mas complejo es tu codigo.
>
3. **El elif:**
*Elif permite comprobar una condición adicional si la condición anterior no se cumplió.*
```python
nota = 5
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("Aprobado!")
else:
    print("¡Suspendido!")
```
*Es decir elif lo que hace es mira nota =5 entonces mira la primera condicion que es >=9 no la cumple pasa a la siguiente, nota >=7 no la cumple, pasa a la siguiente nota >= 5 si la cumple, entonces imprimira Aprobado.*
*Siempre mirara las condiciones por orden y cuando encunetre la primera que se cumpla ya imprimira esa y las demas las ignorara, es decir si nota = 9. 9 es mayor que siete si pero hay una condicion por encima que es >=9 asi que cojera esa.*
*Esto sirve por ejemplo si es 8 que es mayor que siete pero menor a 9 entonces coje la elif nota >=7.*
## Operadores lógicos.
4. **Condiciones múltiples:and**
```python
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
     print("Puedes conducir🚗")
else:
    print("POLICIA 🚓🚓!!!!")
```
*Esto lo que hace es si edad es >= 18 y tiene carnet entonces pasa esto, sino pasa esto otro.*
*Diferencia con el if, que aqui se han de cumplir las dos condiciones la del if es decir edad y la de tiene_carnet. en este caso tiene 25 y tiene_carnet.*
*Pero si fuera edad 25 pero no tine carnet entonces no cumple las dos asi que imprimiria policia.*
- **Condiciones múltiples or:**
```python
edad = 25
tiene_carnet = True
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
```
- **Condición negativa:**
```python
es_fin_de_semana = False
if not es_fin_de_semana:
    print("Toca trabajar!!")
```
--------------------------------------------------
# Operadores de comparación:
```bash
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)
```

```bash
print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera") # True
#Esto da true ya qeu compara manzana la primera letra la m y viene antes de la p de pera por eso es True que es mas grande.
print("'Hola' == 'hola'", "Hola" == "hola") # False
#Esto da false ya que detecta que no son guales ya que la H una es mayuscula y la otra es minuscula. 
```
```bash
# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # si los dos se cumplen da True
print("True and False:", True and False)  # si solo se cumple uno da False
print("True or False:", True or False)    #  con que uno de lso dos se cumple da True
print("False or False:", False or False)  # si ninguni de los dos se cumple da False
print("not True:", not True)             # Fsi es true pasa a ser False
print("not False:", not False)            # si es false pasa a ser True.
```
-------------
# 6.1 Tipos de datos evaluados como Booleanos.
```bash
numero = 5
if numero: # True porque el numero 5 cuando se evalua como una condición booleana es true
    print("El numero no es cero")
numero = 0
if numero: # False el numero 0 cuando se evalua como booleano da false
    print("Aqui no entrara nunca")
```
*Lo mismo con las cadenas de texto.*
```bash
nombre = "Juan"
if nombre:
    print("el nombre no esta vacio")
# Ya que si hay algo escrito lo detecta como True entonces se cumple la condición, si no hay nada escrito pero hay un espacio " " también lo detecta como True. ahora si no hay nada "" lo detecta como False entonces la condición no se cumple.
```
*Separar si es una condición o si es una comparación.*
```bash
numero = 5 #Condición se aplican las normas .
numero == 3 #Comparación.
#Si quieres hacer una condicionde una comparación:
es_el_tres = numero == 3
if es_el_tres:
    print("El numero tres")
```
----------------
# 7. Operadores Ternarios.
*Es una forma concisa de un if-else en una línea de codigo*
*[Codigo si cumple la condición] if [condición] else [codigo si no cumple la condición]*

```python
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "es menor de edad"
print(mensaje)
```
# 8.  Para Hacer comandos de shel a python se usa el modulo import os:
*Esto sirve para que tu al ejecutar el codigo en un sistema operativo te cargue solo el codigo que este dentro de la libreria de import os, y asi no tenga que cargar todo el codigo*
```python
import os
os.system('ls -l')

```
**Para hacerlo con guardando a salida:**
```python
import os
stream = os.popen('ls -l')
sortida = stream.read()
print("sortida", sortida)
```