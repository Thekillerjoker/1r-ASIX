n = int(input())
entrades = []
for i in range(n):
    text = input().strip()
    entrades.append(text)
for paraula in entrades:
    comptador = 0
    for lletra in paraula:
        if lletra.islower():
            comptador += 1
    print(f"{comptador}")
