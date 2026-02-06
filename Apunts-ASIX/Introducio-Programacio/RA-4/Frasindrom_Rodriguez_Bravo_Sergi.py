frase = input().strip()
while frase != ".":
    paraules = frase.split()
    es_capicua = True
    i = 0
    j = len(paraules) -1
    while i < j:
        if paraules[i] != paraules[j]:
            es_capicua = False
        i += 1
        j -= 1
    if es_capicua:
        print("SI")
    else:
        print("NO")
    frase = input().strip()
