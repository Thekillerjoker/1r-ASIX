EMPAT = 0
PEDRA = 1
PAPER = 2
TISORA = 3




def qui_guanya(tria_jugador1, tria_jugador2):
   if ((tria_jugador1 == PEDRA and tria_jugador2 == PAPER) or
           (tria_jugador1 == PAPER and tria_jugador2 == TISORA) or
           (tria_jugador1 == TISORA and tria_jugador2 == PEDRA)):
       guanya = "Jugador2"
   elif ((tria_jugador2 == PEDRA and tria_jugador1 == PAPER) or
         (tria_jugador2 == PAPER and tria_jugador1 == TISORA) or
         (tria_jugador2 == TISORA and tria_jugador1 == PEDRA)):
       guanya = "Jugador1"
   elif (tria_jugador1 == tria_jugador2 and
         tria_jugador1 in [PEDRA, PAPER, TISORA]):
       return EMPAT
   else:
       guanya = "ERROR"
   return guanya




tria_jugador1 = int(input())
tria_jugador2 = int(input())

resultat = qui_guanya(tria_jugador1, tria_jugador2)
print(resultat)

#Se tiene que hacer con if debajo y arriba el error = -1 y el else : guanya = "Error"