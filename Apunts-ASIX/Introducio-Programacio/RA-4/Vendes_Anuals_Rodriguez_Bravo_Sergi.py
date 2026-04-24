casos = int(input())
for x in range(casos):
    vendes = list(map(int, input().split()))
    minim = int(input())
    
    resposta = "SI"
    mes_error = 0

    totes_iguals = True
    
    i = 0
    while i < 12 and resposta == "SI":
        if vendes[i] < minim:
            resposta = "NO"
            mes_error = i + 1
            
        elif i > 0 and vendes[i] < vendes[i - 1]:
            resposta = "NO"
            mes_error = i + 1
        elif i > 0 and vendes[i] != vendes[i - 1]:
            totes_iguals = False
        i += 1
    if resposta == "NO":
        print("NO", mes_error)
    elif totes_iguals:
        print("IGUAL")
    else:
        print("SI")