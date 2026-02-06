n = int(input())
entradas = []
for i in range(n):
    text = input().strip()
    entradas.append(text)
for paraula in entradas:
    if paraula.lower() == "patata":
        print("Es patata")
    else:
        print("No es Patata")
