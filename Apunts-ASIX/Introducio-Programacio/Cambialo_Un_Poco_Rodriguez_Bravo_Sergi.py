casos = int(input())

for i in range(casos):
    k = int(input())
    entrada = input().split()
    p1, p2 = map(int, input().split())

    array = list(map(int, entrada))

    for x in range(k):
        if array[x] == p1:
            array[x] = p2

    for x in range(k):
        print(array[x], end=" ")
    print()