def diamants_al_passadis(pas):
    total = 0
    posicio = 0
    
    while posicio < len(pas) - 1:
        if pas[posicio] == '{' and pas[posicio + 1] == '}':
            total += 1
            posicio += 2
        else:
            posicio += 1

    return total


nombreDeCasos = int(input())
while nombreDeCasos > 0:
    diamants = 0
    nombreDePassadissos = int(input())
    
    for nombreDePassadis in range(nombreDePassadissos):
        passadis = input()
        diamants = diamants + diamants_al_passadis(passadis)
    
    nombreDeCasos = nombreDeCasos - 1
    print(diamants)