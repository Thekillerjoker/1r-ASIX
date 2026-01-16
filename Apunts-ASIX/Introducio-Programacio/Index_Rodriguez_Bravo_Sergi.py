casos = int(input())

for i in range(casos):
    k = int(input())
    entrada = input().split()
    foli = int(input())

    array = list(map(int, entrada))

    posicio = -1

    for x in range(k):
        if array[x] == foli and posicio == -1:
            posicio = x

    print(posicio)
# Hacerlo con un while
