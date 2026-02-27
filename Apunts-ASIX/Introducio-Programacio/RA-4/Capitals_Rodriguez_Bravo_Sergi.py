t = int(input())
for x in range(t):
    N = int(input())
    capitals = {}
    for i in range(N - 1):
        linea = input()
        pais, capital = linea.split("-")
        capitals[pais] = capital
    consulta = input()
    if consulta in capitals:
        print(capitals[consulta])
    else:
        print("NO HO SE")