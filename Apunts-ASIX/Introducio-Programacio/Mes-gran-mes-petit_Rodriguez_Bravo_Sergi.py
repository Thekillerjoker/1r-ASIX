numero = int(input())
minim = numero
maxim = numero
while numero != 0:
    if numero > minim:
        minim = numero
    elif numero < maxim:
        maxim = numero
    numero = int(input())
print(minim, maxim)
