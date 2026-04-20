casos = int(input())
for x in range(casos):
    k = int(input())
    entrada = input().split()
    p = int(input())
    
    array = list(map(int, entrada))
    comptador = 0
    for i in range(k):
        if array[i] == p:
            comptador += 1
    print(comptador)