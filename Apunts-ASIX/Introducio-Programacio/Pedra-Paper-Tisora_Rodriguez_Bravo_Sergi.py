jugador1 = int(input())
jugador2 = int(input())

if jugador1 == 1 and jugador2 == 2 :
    print("Jugador2")
elif jugador1 == 2 and jugador2 == 1:
    print("Jugador1")
elif jugador1 == 1 and jugador2 == 1:
    print("EMPAT")
elif jugador1 == 2 and jugador2 == 2 :
    print("EMPAT")
elif jugador1 == 3 and jugador2 == 3 :
    print("EMPAT")
elif jugador1 == 1 and jugador2 == 3 :
    print("Jugador1")
elif jugador1 == 3 and jugador2 == 1 :
    print("Jugador2")
elif jugador1 == 2 and jugador2 == 3 :
    print("Jugador2")
elif jugador1 == 3 and jugador2 == 2 :
    print("Jugador1")
else :
    print("ERROR")