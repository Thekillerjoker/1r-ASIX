n = int(input())
for linea in range(1,n + 1):
    resultat = ""
    for repeticio in range(1, linea + 1):
       if repeticio == 1:
           resultat += str(repeticio)
       else:
           resultat += ", " + str(repeticio)
    print(resultat)