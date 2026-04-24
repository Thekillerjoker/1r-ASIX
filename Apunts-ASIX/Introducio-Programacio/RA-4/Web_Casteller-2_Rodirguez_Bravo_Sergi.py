casos = int(input())

for _ in range(casos):
    frase1 = input().split()
    frase2 = input().split()

    correcte = True

    for p in range(len(frase1)):
        paraula1 = frase1[p]
        paraula2 = frase2[p]

        llargada = max(len(paraula1), len(paraula2))
        iguals = 0

        for i in range(min(len(paraula1), len(paraula2))):
            if paraula1[i] == paraula2[i]:
                iguals += 1

        if iguals * 2 < llargada:
            correcte = False

    if correcte:
        print("GRACIES WEBCASTELLER")
    else:
        print("WEBCASTELLER ESTA TRAVIESO HOY")