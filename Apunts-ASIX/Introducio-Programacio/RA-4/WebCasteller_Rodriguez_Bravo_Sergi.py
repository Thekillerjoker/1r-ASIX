casos = int(input())

for x in range(casos):
    paraules = []

    paraules.append(input().strip())
    paraules.append(input().strip())

    dita = paraules[0]
    resposta = paraules[1]

    llargada = max(len(dita), len(resposta))
    iguals = 0

    for i in range(min(len(dita), len(resposta))):
        if dita[i] == resposta[i]:
            iguals += 1

    if iguals * 2 >= llargada:
        print("GRACIES WEBCASTELLER")
    else:
        print("WEBCASTELLER ESTA TRAVIESO HOY")