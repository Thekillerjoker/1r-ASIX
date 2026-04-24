casos = int(input())
for x in range(casos):
    paraula = input().strip()
    trobat = False
    i = 0
    
    while i < len(paraula) - 1 and not trobat:
        if paraula[i] == paraula[i + 1]:
            trobat = True
        i += 1
    if trobat:
        print("SI")
    else:
        print("NO")