import os

usuaris = {
    "root": ["systemd", "sshd", "cron"],
    "sergi": ["ls", "cd", "python"]
}

Entrada = input("Introdueix un usuari i la comanda amb arguments si cal: ").strip()
parts = Entrada.split()
if len(parts) < 2:
    print("Error cal indicar l'usuari i la comanda.")
else:
    usuari = parts[0]
    comanda = parts[1]
    arguments = parts[2:]
    if usuari not in usuaris:
        print("Error: usuari no existeix.")
    else:
        if comanda in usuaris[usuari]:
            comanda_completa = " ".join(parts[1:])
            sortida = os.popen(comanda_completa).read()
        else:
            print("Error: Aquesta comanda no està permesa per auest usuari.")
