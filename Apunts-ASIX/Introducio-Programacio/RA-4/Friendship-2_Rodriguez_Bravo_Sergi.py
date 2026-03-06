Casos = int(input('Introdueix el nombre de Cassos:' ))
resultats = []
for i in range(Casos):
    linies = int(input('Introdueix el numero de línies:' ))
    amics = {}
    for x in range(linies - 1):
        a, b = input().split()
        amics[a] = b
        amics[b] = a
    consulta = input('Introdueix el nombre a consultar:' )
    resultats.append(amics[consulta])
for r in resultats:
    print(r)