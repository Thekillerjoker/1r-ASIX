casos = int(input())
for x in range(casos):
    k = int(input())
    entrada = input().split()
    p = int(input())
    for i in range(k):
        array = list(map(int, entrada))
        array[i]  = array[i] * p
        print(array[i], end=" ")
    print()