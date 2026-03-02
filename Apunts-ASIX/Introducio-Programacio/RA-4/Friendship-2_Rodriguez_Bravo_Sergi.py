Casos = int(input())
resultats = []
for i in range(Casos):
    linies = int(input())
    amics = {}
    for x in range(linies - 1):
        a, b = input().split()
        amics[a] = b
        amics[b] = a
    consulta = input()
    resultats.append(amics[consulta])
for r in resultats:
    print(r)