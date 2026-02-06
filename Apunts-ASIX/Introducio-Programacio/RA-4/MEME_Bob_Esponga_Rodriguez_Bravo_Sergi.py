n = int(input())
frases = []
for i in range(n):
    frases.append(input())
for frase in frases:
    resultat = ""
    comptador = 0
    for c in frase:
        if c == " ":
            resultat += " "
        else:
            if comptador % 2 == 0:
                resultat += c.lower()
            else:
                resultat += c.upper()
            comptador += 1
    print(resultat)
