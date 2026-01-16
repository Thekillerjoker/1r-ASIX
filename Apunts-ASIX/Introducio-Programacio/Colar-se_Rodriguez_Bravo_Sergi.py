casos = int(input())

for i in range(casos):
    k = int(input())
    entrada = input().split()
    c, p = map(int, input().split())

    array = list(map(int, entrada))

    resultat = [0] * (k + 1)

    for x in range(p):
        resultat[x] = array[x]

    resultat[p] = c

    for x in range(p, k):
        resultat[x + 1] = array[x]

    for j in resultat:
        print(j, end=" ")
    print()