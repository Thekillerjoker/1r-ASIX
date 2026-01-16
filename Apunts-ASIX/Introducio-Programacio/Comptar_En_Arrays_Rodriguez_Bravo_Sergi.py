casos = int(input("Introdueix el nombre de casos desitjats:" ))
for i in range(casos):
    k = int(input("Quantitat de numeros que contindra l'array:" ))
    entrada = input("Introdueix K nombres del 0 al 100: ").split()
    p = int(input("Intordueix el nombre que vols comprovar si esta a la llista: "))
    array = list(map(int, entrada))
    comptador = 0
    for x in range(k):
        if array[x] == p:
            comptador += 1
    print(comptador)