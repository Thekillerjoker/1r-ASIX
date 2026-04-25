# Explicaciones
## 🧠 1. La clave: traducir el enunciado

**Cuando lees un ejercicio, haz SIEMPRE esto:**

***🔹 Paso 1: ¿Qué me dan?***

*👉 datos de entrada*
- **números** → variables
- **lista de números** → array (lista)
- **texto** → string

***🔹 Paso 2: ¿Qué tengo que hacer?***

*👉 proceso*
- **contar** → bucle
- **buscar** → bucle
- **comparar** → if
- **transformar** → bucle + if

***🔹 Paso 3: ¿Qué tengo que mostrar?***

*👉 print*

## 🧱 2. Cuándo usar cada cosa

### 📦 Arrays (listas)

*👉 cuando hay MUCHOS datos del mismo tipo*

Ejemplo:
```python
6
17 20 24 5 1 10
```

👉 esto = lista
```python
edats = list(map(int, input().split()))
```
*
---
### 🔁 Bucles (`for / while`)

*👉 cuando tienes que repetir algo*
- **recorrer lista** → `for`
- **repetir hasta condición** → `while`
*
---
### 🔤 Strings

*👉 cuando trabajas con texto*

**Ejemplo:**
```python
bloodborne
```

- **recorrer letras** → bucle
- **comparar** → if
- **usar funciones** (`lower`, `isalnum`, etc.)
*
---
### 📚 Diccionarios

*👉 cuando tienes clave → valor*

**Ejemplo:**
```python
nombre → edad
d = {"Sergi": 20}
```
*👉 en tus ejercicios actuales → casi no los necesitas aún*
*
---

## 🧩 3. Cómo plantear un ejercicio (plantilla mental)

*Usa SIEMPRE esta estructura:*

 1. leer datos
 2. preparar variables
 3. bucle (si hace falta)
 4. condiciones (if)
 5. print
*
---
## 🔥 4. Ejemplo real paso a paso
**Enunciado:**
*“contar cuántos son menores que X”*

*🧠 Pensamiento:*
- **hay muchos números** → lista
- **hay que contar** → variable contador
- **hay que recorrer** → bucle

**💻 Código:**
```python
edats = list(map(int, input().split()))
X = int(input())

contador = 0

for e in edats:
    if e < X:
        contador += 1

print(contador)
```
*
---

## 🧠 5. Cómo saber si usar bucle

***Pregúntate:***

*👉 “¿Tengo que mirar uno a uno?”*

✔ **SÍ** → bucle
❌ **NO** → no hace falta
---

## 🧠 1. Leer el enunciado como un programador
**Entrada**

*Te dicen:*
**K** → tamaño del array
**K números** → contenido del array
**N** → posición

***👉 Traducción mental:***

**K** → un número normal
**K números**→ 👉 ARRAY (lista)
**N** → otro número
*
---

## 🧱 2. ¿Qué tengo que guardar?

***👉 Variables:***

- **K** → tamaño (aunque casi ni lo necesitas)
- **array** → lista de números
- **N** → índice

## 🔍 3. ¿Qué tengo que hacer?

### Parte 1:

*“mostrar el array entero”*

**👉 Eso es:**

**recorrer el array** → 🔁 bucle

### Parte 2:

*“mostrar el valor en la posición N”*

**👉 Eso es:**

- **acceder directamente** → ❌ NO bucle
- **simplemente:** posición concreta
*
---

## ⚖️ 4. Decisiones importantes

***❓ ¿Uso array?***

- **✔ SÍ** → porque hay muchos números

***❓ ¿Uso bucle?***

- **✔ SÍ**→ para imprimir todo el array
- **❌ NO** → para acceder a una posición
*
---

## 🧠 5. Esquema mental del ejercicio
1. leer K
2. leer array
3. leer N

4. recorrer array → imprimirlo
5. acceder a array[N] → imprimirlo
*
---
## 🔥 6. Cómo detectar esto en un examen

**Cuando veas:**

- **“K números”** → 👉 ARRAY
- **“mostrar todos”** → 👉 FOR
- **“posición N”** → 👉 acceso directo
*
---

## ⚠️ 7. Error típico que debes evitar
- **usar bucle para buscar N** → ❌ mal
    - 👉 aquí no buscas, ya te dan la posición
*
---
## 🎯 8. Regla clave que debes aprender

- **👉 Array** = muchos datos
- **👉 For** = recorrer todos
- **👉 [N]** = acceder a uno
*
---

## 🧠 Hay 2 formas de hacer un for
*🔹 1. Recorrer valores (la MÁS usada)*

👉 cuando solo quieres ver los elementos
```python
for x in array:
```
**x =** cada valor del array
no usas posiciones

*🔹 2. Recorrer posiciones (índices)*

👉 cuando necesitas saber la posición

for i in range(len(array)):
i = posición (0, 1, 2…)
accedes con → array[i]

### 🔥 ¿Cuál usar en TU ejercicio?

**El enunciado dice:**

*👉 “mostrar el array entero”*

➡️ NO necesitas posiciones
➡️ solo quieres imprimir valores

*✔ Entonces usas:*

👉 for x in array

⚠️ ¿Cuándo usarías el otro?

Usas:

for i in range(len(array)):

cuando necesitas:

- comparar posiciones
- modificar el array
- acceder a varios índices

### 🧠 Truco mental definitivo

**Hazte esta pregunta:**

- ❓ ¿Necesito la posición?
- ❌ NO → for x in array
- ✔ SÍ → for i in range(...)

>[!TIP]- Pregunta
>ya lo tengo resuelto y es k = int(input()) array = list(map(int, input().split())) n = int(input()) for x in array: print(x, end=" ") print() print(array[n]) ahora la cosa es como he de saber que el print es print(x, end=" ") y no print(array[x], end=" ") o print(array, end=" ") ?
>

### 🧠 ¿Qué es x en for x in array?

**Cuando haces:**
```python
for x in array:
```

- 👉 x NO es la posición
- 👉 x ES el valor

***Ejemplo***:
```python
array = [10, 20, 30]
```

*El bucle hace:*
```python
x = 10
x = 20
x = 30
```

#### 🔥 Entonces…
***✔ Correcto:***
```python
print(x, end=" ")
```

*👉 porque x ya es el número*

***❌ Incorrecto:***
```python
print(array[x], end=" ")
```
*👉 porque aquí estás diciendo:*

*`“usa x como índice”`*

*Ejemplo real:*
```python
x = 10 → array[10] ❌ error
```

***❌ Incorrecto:***
```python
print(array, end=" ")
```
*👉 imprime toda la lista:*
```python
[10, 20, 30]
```

## 🧠 Regla de oro (importantísima)

**👉 Si usas:**
```python
for x in array:
```
*✔ usa `x`*
---

**👉 Si usas:**
```python
for i in range(len(array)):
```

*✔ usa `array[i]`*
---

## 🔁 Comparación clara

***Forma 1 (valores)***
```python
for x in array:
    print(x)
```

***Forma 2 (posiciones)***
```python
for i in range(len(array)):
    print(array[i])
```

*👉 hacen lo mismo, pero cambian las variables*

## 🎯 Truco mental definitivo

***Pregúntate:***

*`👉 “¿x es valor o índice?”`*

- **for x in array** → `valor`
- **for i in range(...)** → `índice`

*
---
>[!IMPORTANT]- EX2
>El problema serà de tres línies. La primera tindrà un nombre, K que et dirà el tamany de l'array que has de crear La segona son K nombres, separats per espais que et dirà el contingut de l'array que has de llegir. La tercera serà N, un valor a sumar a tots els elements de l'array Sortida Tornaràs l'array sencer escrit, amb espais entre cada caràcter, després d'haver sumat N a cada posició. Exemple d'Entrada Copy 6 23 2 -4 0 42 69420 2 Exemple de Sortida Copy 25 4 -2 2 44 69422
>
*
---

## 🧠 1. ¿Qué me dan?

- **K** → tamaño (no muy importante)
- **lista de números**→ 👉 ARRAY
- **N** → número a sumar

## 🧠 2. ¿Qué tengo que hacer?

**👉 “sumar N a todos los elementos”**

*Traducción mental:*

`recorrer array → sumar N → mostrar resultado`

## 🧱 3. ¿Qué necesito usar?

- **✔ array** → porque hay muchos números
- **✔ bucle** → porque tienes que modificar TODOS
*
---

## 🔥 4. Tipo de bucle → AQUÍ está la clave

**Pregúntate:**

*👉 “¿Tengo que cambiar los valores?”*

- **✔ SÍ** → necesitas posiciones

*👉 entonces:*

`usar for con índices`

### ⚠️ IMPORTANTE

**Aquí hay dos formas de hacerlo:**

***🟢 OPCIÓN 1 (la más simple mentalmente)***

- *👉 no modificas el array, solo imprimes*

*recorres valores → sumas → imprimes*

***👉 usarías:***
`for x in array`


***🔵 OPCIÓN 2 (más “formal”)***

- *👉 modificas el array*

`array[i] = array[i] + N`

- *👉 usarías:*

`for i in range(...)`

*
---

## 🧠 5. Estructura mental final
1. leer K
2. leer array
3. leer N

4. recorrer array
   - → sumar N
   - → mostrar resultado

*
---

## 🎯 6. Cómo saber qué for usar (CLAVE)

**👉 pregúntate:**

| Situación       | Bucle               |
|-----------------|---------------------|
| solo imprimir   | for x in array      |
| modificar array |	for i in range(...) |

```python
k = int(input())
array = list(map(int, input().split()))
N = int(input())
for i in range(k):
    array[i] = array[i] + N
    print(array[i], end=" ")
```
*
---

>[!IMPORTANT]- EX-3
>Entrada
>La primera línia indica els casos de prova a considerar Cada cas conté tres linies. La primera té un nombre K. La segona conté K nombres del 0 al 100. La tercera conté un nombre P<K
>Sortida
>Per cada cas de prova es vol retornar el nombre que ocupava la posició P en la llista de nombres. Considereu que la primera posició és 0.
>Exemple d'Entrada
>2
>3
>1 2 3
>0
>5
>5 6 7 8 9
>2
>Exemple de Sortida
>1
>7
>

🧠 2. Traducción mental

Por cada caso:

leer K
leer lista de K números
leer P (posición)

🧠 3. ¿Qué te piden?

“retornar el nombre que ocupava la posició P”

👉 Traducción:

quiero el valor en la posición P del array
🔥 4. CLAVE del ejercicio

👉 NO tienes que:

buscar ❌
recorrer ❌
contar ❌

👉 SOLO tienes que:

acceder a una posición concreta
🧠 5. Pregunta clave que debes hacerte

👉 “¿Ya me dan la posición?”

✔ SÍ → entonces NO necesitas bucle

*
---

>[!IMPORTANT]-Index de
>La primera línia indica els casos de prova a considerar Cada cas conté tres linies. La primera té un nombre K. La segona conté K nombres del 0 al 100. La tercera conté un nombre FOLI.S'ha de tornar la posició del foli que és igual a FOLI. En cas d'haver folis repetits, torna la posició del primer. Considera que les posicions comencen per 0. Si el foli no està, torna -1
>
*
---
## Cuando usar .index()

***Usa .index() cuando el enunciado te pida:***

*“dime la posición de un valor dentro de una lista/string”*

La palabra clave mental es:

`valor → posición`


***Cuándo usar `.index()`***

*Si lees cosas como:*
```
Troba la posició de X
Retorna l’índex de X
En quina posició apareix X?
Si està repetit, retorna el primer
```

*Entonces `.index()` encaja muy bien.*

*Porque `.index()` hace exactamente esto:*
```
busca un valor y devuelve su primera posición
```

***Cuándo NO usar `.index()`***

*No lo uses si te piden:*
```
mostrar todos los valores
sumar todos los valores
contar cuántas veces aparece
modificar todos los elementos
buscar todas las posiciones
```

*Ahí normalmente necesitas un bucle.*

### Regla rápida

| Enunciado dice...	       | Piensa...	         | Herramienta          |
|--------------------------|---------------------|----------------------|
| “posición de un valor”   | valor → posición    |	`.index()`          |
| “valor en una posición”  |	posición → valor |	`array[pos]`        |
| “cuántas veces”          |	contar           | `.count()` o bucle   |
| “todos los elementos”    | recorrer            | `for`                |
| “cambiar elementos”      |	modificar        |	bucle con índices   |

*
---

## Ex T'enrecordes de :

No poner for x in range(array):

Range solo acepta numeros no listas

enb ese caso poner for x in range(k)


## Cambiar valores de un array por otros:
```python
casos = int(input())
for x in range(casos):
    K = int(input())
    array = list(map(int, input().split()))
    P1,P2 = map(int, input().split())
    for i in range(K):
        if array[i] == P1:
            array[i]= P2
    for i in range(K):
        print(array[i], end=" ")
    print()
```


## Colarse es decir insertar valores:
```python
casos = int(input())

for _ in range(casos):
    k = int(input())
    array = list(map(int, input().split()))
    c, p = map(int, input().split())

    array.insert(p, c)

    print(*array)
```
🧠 Qué hace
array.insert(p, c) → mete c en la posición p
desplaza automáticamente el resto
print(*array) → imprime como 1 2 3 (sin corchetes)

## stings dos bucles
```python
n = int(input())
entrades = []
for i in range(n):
    text = input().strip()
    entrades.append(text)
for paraula in entrades:
    comptador = 0
    for lletra in paraula:
        if lletra.islower():
            comptador += 1
    print(f"{comptador}")
```


## Strings
🧠 1. “Es patata”
🧠 Pensamiento
tengo un string
quiero comparar con "patata"
ignorando mayúsculas
💻 Código
n = int(input())

for _ in range(n):
    paraula = input().strip()

    if paraula.lower() == "patata":
        print("Es Patata")
    else:
        print("No es Patata")
🧠 2. Contar minúsculas
🧠 Pensamiento
tengo un string
quiero mirar letra a letra
quiero contar las minúsculas
💻 Código
n = int(input())

for _ in range(n):
    paraula = input().strip()
    comptador = 0

    for c in paraula:
        if c.islower():
            comptador += 1

    print(comptador)
🧠 3. Alternar minúscula/mayúscula
🧠 Pensamiento
tengo un string
quiero transformarlo
ignoro espacios
construyo uno nuevo
💻 Código
n = int(input())

for _ in range(n):
    frase = input()
    resultat = ""
    comptador = 0

    for c in frase:
        if c == " ":
            resultat += " "
        else:
            if comptador % 2 == 0:
                resultat += c.lower()
            else:
                resultat += c.upper()
            comptador += 1

    print(resultat)
🧠 4. Frase capicua
🧠 Pensamiento
tengo una frase
la separo en palabras
comparo principio y final
💻 Código
frase = input().strip()

while frase != ".":
    paraules = frase.split()
    es_capicua = True

    i = 0
    j = len(paraules) - 1

    while i < j:
        if paraules[i] != paraules[j]:
            es_capicua = False
        i += 1
        j -= 1

    if es_capicua:
        print("SI")
    else:
        print("NO")

    frase = input().strip()
🔥 AHORA LO IMPORTANTE
🧠 5. Patrón general que debes ver

Todos tus ejercicios siguen esto:

leer string
recorrer
hacer algo (comparar / contar / transformar)
print
🎯 6. Cómo decidir qué hacer (con código)
Enunciado dice	Pensamiento	Código
“es igual a”	comparar	==
“cuántos hay”	contar	contador
“cambiar”	transformar	string nuevo
“palabras”	dividir	split()
🚀 7. CLAVE FINAL

👉 Antes de escribir código, piensa:

¿voy a recorrer?
¿voy a comparar?
¿voy a transformar?

## Diccioanris:

Sí. En diccionarios la idea clave es esta:

clave → valor

Usas diccionario cuando el enunciado dice algo como:

nombre → cumpleaños
país → capital
persona → mejor amigo
mapa → votos
1. Nombre → cumpleaños
Razonamiento

Te dan varios nombres y fechas. Luego te dan un nombre y tienes que buscar su fecha.

clave = nom
valor = data
Código sin textos en los input
n = int(input())
dades = {}

for _ in range(n):
    nom = input()
    data = input()
    dades[nom] = data

consulta = input()

elements = []
for nom, data in dades.items():
    elements.append(f"{nom}={data}")

sortida = "{" + ", ".join(elements) + "}"

print(sortida)
print(dades[consulta])
2. País → capital
Razonamiento

Cada línea tiene:

PAIS-CAPITAL

Luego preguntan por un país.

clave = país
valor = capital

Si no existe, imprimir "NO HO SE".

t = int(input())

for _ in range(t):
    n = int(input())
    capitals = {}

    for _ in range(n - 1):
        linea = input()
        pais, capital = linea.split("-")
        capitals[pais] = capital

    consulta = input()

    if consulta in capitals:
        print(capitals[consulta])
    else:
        print("NO HO SE")
3. Persona → mejor amigo
Razonamiento

Cada línea dice:

persona amigo

El segundo es el mejor amigo del primero.

clave = persona
valor = amic

Si aparece otra vez la misma persona, se actualiza el valor porque “importa el último”.

t = int(input())

for _ in range(t):
    k = int(input())
    amics = {}

    for _ in range(k - 1):
        persona, amic = input().split()
        amics[persona] = amic

    consulta = input()
    print(amics[consulta])
4. Amistad mutua
Razonamiento

Ahora la relación es doble:

A B

significa:

A → B
B → A

Por eso guardas las dos direcciones.

casos = int(input())

for _ in range(casos):
    linies = int(input())
    amics = {}

    for _ in range(linies - 1):
        a, b = input().split()
        amics[a] = b
        amics[b] = a

    consulta = input()
    print(amics[consulta])
5. Mapa → número de votos
Razonamiento

Aquí el diccionario sirve para contar.

clave = mapa
valor = número de votos

Cada vez que aparece un mapa, sumas 1.

casos = int(input())

for _ in range(casos):
    k = int(input())
    vots = {}

    for _ in range(k):
        mapa = input()

        if mapa in vots:
            vots[mapa] += 1
        else:
            vots[mapa] = 1

    max_vots = 0
    mapa_guanyador = ""

    for mapa, quantitat in vots.items():
        if quantitat > max_vots:
            max_vots = quantitat
            mapa_guanyador = mapa

    print(mapa_guanyador)
6. Mapa con votos al final
Razonamiento

Cada línea tiene:

nombre del mapa con espacios + número final

Ejemplo:

Desierto del Sinaí 2

La última parte es el número, y todo lo anterior es el nombre.

clave = mapa
valor = votos acumulados
casos = int(input())

for _ in range(casos):
    k = int(input())
    vots = {}

    for _ in range(k):
        entrada = input()
        parts = entrada.split()

        grup = int(parts[-1])
        mapa = " ".join(parts[:-1])

        if mapa in vots:
            vots[mapa] += grup
        else:
            vots[mapa] = grup

    max_vots = 0
    mapa_guanyador = ""

    for mapa, quantitat in vots.items():
        if quantitat > max_vots:
            max_vots = quantitat
            mapa_guanyador = mapa

    print(mapa_guanyador)
Cómo razonar diccionarios en enunciados

Cuando leas un enunciado, busca si hay una relación de este tipo:

A tiene B
A corresponde a B
A se traduce como B
A acumula puntos
A aparece varias veces

Entonces probablemente es diccionario.

La pregunta clave es:

¿qué uso como clave?
¿qué guardo como valor?

Ejemplos:

nombre → fecha
país → capital
persona → amigo
mapa → votos
producto → precio
alumno → nota
palabra → veces que aparece

Regla rápida:

Si quiero buscar rápido por nombre, país, persona o mapa → diccionario.
Si quiero contar cuántas veces aparece algo → diccionario.
Si quiero actualizar el último valor de alguien → diccionario.

## Comandes amb arrays:

🧠 1. ¿Qué tipo de ejercicio es?

👉 No es de cálculo
👉 No es de strings complejos

👉 Es de:

leer datos → guardarlos → recorrer → ejecutar algo

🧠 2. ¿Qué te dan?
un número N
N nombres de hosts

👉 Traducción:

muchos datos del mismo tipo → ARRAY

🧱 3. ¿Qué tienes que hacer?

hacer 2 pings a cada host
mostrar resultado

🧠 4. Traducción mental COMPLETA

1. leer N
2. leer N hosts → guardarlos en array
3. recorrer array
4. para cada host:
       hacer ping 2 veces
       mostrar resultado

🔥 5. CLAVE del ejercicio

👉 Es un patrón muy típico:

guardar datos → recorrer → hacer acción

🧠 6. ¿Dónde va el array?

👉 Aquí:

cuando lees los hosts

👉 porque:

tienes varios elementos → necesitas almacenarlos

🧠 7. ¿Cuántos bucles hay?

👉 2 posibles formas de pensarlo:

✔ Opción normal
1 bucle → leer hosts
1 bucle → recorrer hosts
✔ Opción compacta (más avanzada)

leer + procesar en el mismo bucle

🧠 8. Pregunta clave

👉 “¿Tengo que hacer algo con TODOS los elementos?”

✔ SÍ → necesitas bucle

🧠 9. Qué acción haces dentro del bucle
por cada host:
    ejecutar ping (2 veces)

⚠️ 10. Lo importante aquí

👉 No es un problema de arrays complicado
👉 Es un problema de:

recorrer lista + ejecutar comando

🎯 11. Cómo reconocer este tipo en examen

Si ves:

N elementos
hacer algo con cada uno

👉 automáticamente piensa:

array + for

🚀 12. Resumen final (muy importante)

leer N

guardar N elementos en array

recorrer array

hacer acción con cada elemento

💡 Frase clave

👉 “si tengo muchos datos y hago lo mismo con todos → array + for”
```python
import os
N = int(input())
hosts = []
for x in range(N):
    entrada = input()
    hosts.append(entrada)
for entrada in hosts:
    os.system(f"ping -c 2 {entrada} ")
```
