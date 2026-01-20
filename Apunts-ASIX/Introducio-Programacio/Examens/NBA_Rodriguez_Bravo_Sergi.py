puntslocal, equiplocal = input().split()
puntslocal = int(puntslocal)
puntsvisitant, equipvisitant = input().split()
puntsvisitant = int(puntsvisitant)
if puntslocal > puntsvisitant:
    print(equiplocal)
elif puntsvisitant > puntslocal:
    print(equipvisitant)
