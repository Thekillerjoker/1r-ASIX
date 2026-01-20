import os
seleccio = ""
executant = False
while executant == False:
    print("# --- Menu comprovació de Xarxa -------------")
    print("# --- 1: Ping a bing.com ----------------------")
    print("# --- 2: Ping  a google.com -------------")
    print("# --- 3: ping a 8.8.8.8 -----")
    print("# --- 4: Verificar funcionament localhost ---")
    seleccio = int(input("Introdueix l'opció desitjada: "))
    if seleccio == 1:
        os.system('ping -c 4 bing.com ')
        executant = True
    elif seleccio == 2:
        os.system('ping -c 4 google.com ')
        executant = True
    elif seleccio == 3:
        os.system('ping -c 4 8.8.8.8 ')
        executant = True
    elif seleccio == 4:
        os.system('ping -c 4 127.0.0.1 ')
        executant = True
    else:
        print("Intodueix una opcio correcta")
        executant = False