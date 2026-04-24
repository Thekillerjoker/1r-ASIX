casos = int(input())
for x in range(casos):
    K = int(input())
    sabates = list(map(int, input().split()))
    M = int(input())
    
    trobat = False
    
    for i in sabates:
        if i == M or i == M - 1 or i == M + 1:
            trobat = True
    if trobat == True:
        print("SI")
    else:
        print("NO")