casos = int(input())
for x in range(casos):
    k = int(input())
    entrada = input().split()
    p1, p2 = map(int, input().split())
    array = list(map(int, entrada))
    for i in range(k):
        if array[i] == p1:
            array[i] = p2
    for i in range(k):    
        print(array[i], end=" ")
    print()