n = int(input())
resultat = ""
for numero in range(1,n + 1):
    for repeticio in range(1, numero + 1):
        resultat += str(numero)
print(resultat)
