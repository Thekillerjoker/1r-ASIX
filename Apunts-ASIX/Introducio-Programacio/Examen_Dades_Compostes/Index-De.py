#casos = int(input())
#for i in range(casos):
#    k = int(input())
#    entrada = input().split()
#    foli = int(input())
#    array = list(map(int, entrada))
#    posicio = -1
#    for x in range(k):
#        if array[x] == foli and posicio == -1:
#            posicio = x
#    print(posicio)
    
##La forma con .index
Casos = int(input())
for x in range(Casos):
    K = int(input())
    Array = list(map(int, input().split()))
    Foli = int(input())
    if Foli in Array:
        print(Array.index(Foli)) #Retorna la posicio del primer valor repetit
    else:
        print(-1)
