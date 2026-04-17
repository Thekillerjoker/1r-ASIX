def mostra_valors_canviats(nombres, numeroACanviar, numeroAPosar):
    for i in range(len(nombres)):
        if nombres[i] == numeroACanviar:
            nombres[i] = numeroAPosar

    for i in range(len(nombres)):
        print(nombres[i], end=" ")
    print()


def tractar_cas():
   quantitatNumeros = int(input())
   nombres = list(map(int, input().strip().split()))
   numeroACanviar, numeroAPosar = map(int, input().strip().split())
   mostra_valors_canviats(nombres, numeroACanviar, numeroAPosar)


nombreDeCasos = int(input())
while nombreDeCasos > 0:
   tractar_cas()
   nombreDeCasos = nombreDeCasos - 1