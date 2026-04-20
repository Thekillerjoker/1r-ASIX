casos = int(input())
for i in range(casos):
    k = int(input())
    entrada = input().split()
    p = int(input())
    array = list(map(int, entrada))
    print(array[p])