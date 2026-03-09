import os
import time
programa = True
while programa == True:
    sortida = os.popen(f'ps aux ')
    linies = sortida.readlines()

    processos = {}

    for linea in linies[1:]:
        camps = linea.split()
        if len(camps) > 0:
            usuari = camps[0]
            if usuari not in processos:
                processos[usuari] = 1
            else:
                processos[usuari] += 1
                
    usuari_demanat = input('Introdueix el nom d usuari desitjat, per sortir del programa escriu FI: ')
    if usuari_demanat in processos:
        print(f'Nombre de procesos del usuari {usuari_demanat}: {processos[usuari_demanat]}')
    elif usuari_demanat == 'FI' or usuari_demanat == 'Fi' or usuari_demanat == 'fi':
        print('Sortint del programa....')
        time.sleep(2)
        programa = False
    else:
        print('Aquest usuari no existeix....')