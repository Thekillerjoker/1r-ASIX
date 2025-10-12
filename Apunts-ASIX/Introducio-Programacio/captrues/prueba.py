monedes = int(input())
for m in [200, 100, 50, 20, 10, 5, 2, 1]:
    print(monedes // m)
    monedes%=m
    
#-- ejemplo de exercici de les monedes amb operacioons en varaibles---
centims = int(input())
doseuros = centims // 200; centims %= 200
uneuro = centims // 100; centims %= 100
cinquantacentims = centims // 50; centims %= 50
vintcentims = centims // 20; centims %= 20
deucentims = centims // 10; centims %= 10
cinccentims = centims // 5; centims %= 5
doscentims = centims // 2; centims %= 2
uncentim = centims

print(doseuros)
print(uneuro)
print(cinquantacentims)
print(vintcentims)
print(deucentims)
print(cinccentims)
print(doscentims)
print(uncentim)


#---Exercici de les Monedes2---

monedes = int(input())

for map(function, iterables)
centims = int(input())
original = centims  # guardar antes de modificar

doseuros = original // 200; original %= 200
uneuro = original // 100; original %= 100
cinquantacentims = original // 50; original %= 50
vintcentims = original // 20; original %= 20
deucentims = original // 10; original %= 10
cinccentims = original // 5; original %= 5
doscentims = original // 2; original %= 2
uncentim = original

print(f"{centims // 100},{centims % 100:02d} euros =")#:02d formateja el numeros de forma que el resultat es motri minim amb dos xifres.
print(doseuros,"monedes de dos eur")
print(uneuro,"monedes d'un eur")
print(cinquantacentims,"monedes de 50 cts")
print(vintcentims,"monedes de vint cts")
print(deucentims,"monedes de 10 cts")
print(cinccentims,"monedes de cinc cts")
print(doscentims,"monedes de dos cts")
print(uncentim,"monedes d'un cts")

