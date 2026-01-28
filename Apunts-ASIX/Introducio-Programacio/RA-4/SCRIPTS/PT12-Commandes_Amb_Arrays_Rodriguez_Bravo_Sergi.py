import os
n = int(input("Introdueix el numero de hosts al que vols fer ping: "))
hosts = []
for x in range(n):
    entrada = input("Introdueix el nom dels hosts al que vols fer ping: ")
    hosts.append(entrada)
for entrada in hosts:
    os.system(f"ping -c 2 {entrada} ")