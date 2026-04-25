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
