t = int(input())
for casos in range(t):
    numeros = list(map(int, input().split()))
    repetit = None
    for i in range(5):
        repeticions = 0
        for x in range(5):
            if numeros[i] == numeros[x]:
                repeticions += 1
        if repeticions >= 3:
            repetit = numeros[i]
    if repetit != None:
        print(repetit)
    else:
        print("NO")
