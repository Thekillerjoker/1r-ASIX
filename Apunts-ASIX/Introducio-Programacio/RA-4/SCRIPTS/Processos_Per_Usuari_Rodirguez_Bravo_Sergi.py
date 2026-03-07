import os
import time
usuaris = {
    "root": ["systemd", "sshd", "cron", "rm"],
    "sergi": ["ls", "cd", "python"],
    "alumne1": ["pwd", "cat", "echo", "whoami"],
    "perepi": ["mkdir", "date", "rmdir"]
}
Entrada = input("Inrodueix l'usuari i la comanda amb arguments si cal: ").strip()
parts = Entrada.split()
if len(parts) < 2:
    print("Error cal  introduir l'usuari i la comanda.")
    print("Sortint del programa...")
    time.sleep(2)
else:
    usuari = parts[0]
    comanda = parts[1]
    arguments = parts[2:]
    if  usuari not in usuaris:
        print("Error: Usuari no existeix en el diccionari.")
        print("Sortint del programa...")
        time.sleep(2)
    else:
        if comanda in usuaris[usuari]:
            comanda_completa = " ".join(parts[1:])
            print(f"Executant {comanda_completa}...")
            sortida = os.popen(comanda_completa).read()
            print(sortida)
            print("Sortint del programa...")
            time.sleep(2)
        else:
            print("Error: Aquesta comanda no està permesa per aquest usuari.")
            print("Sortint del programa...")
            time.sleep(2)