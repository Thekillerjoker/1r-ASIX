n = int(input())
for linea in range(1,n + 1):
    resultat = ""
    for repeticio in range(linea, 0, -1):
        if repeticio == linea:
            resultat += str(repeticio)
        else:
            resultat += ", " + str(repeticio)
    print(resultat)