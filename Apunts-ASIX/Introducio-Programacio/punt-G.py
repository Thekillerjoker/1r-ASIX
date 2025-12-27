lletra1 = input()
lletra2 = input()
lletra3 = input()
lletra4 = input()
lletra5 = input()
contador = 0
if lletra1 == "G":
    contador += 1
if lletra2 == "G":
    contador += 1
if lletra3 == "G":
    contador += 1
if lletra4 == "G":
    contador += 1
if lletra5 == "G":
    contador += 1
if contador == 0:
    print("NO")
elif contador == 1:
    print("SI")
else:
    print("PUNTOS")