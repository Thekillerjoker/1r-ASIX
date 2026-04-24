casos = int(input())

for x in range(casos):
    cartes = list(map(int, input().split()))

    if 1 in cartes and 10 in cartes and 11 in cartes and 12 in cartes and 13 in cartes:
        print("ESCALA REIAL")
    else:
        escala = False

        for inici in range(1, 10):
            if inici in cartes and inici + 1 in cartes and inici + 2 in cartes and inici + 3 in cartes and inici + 4 in cartes:
                escala = True

        if escala:
            print("ESCALA")
        else:
            print("NO")