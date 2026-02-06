import os
import subprocess

serveis = []
opcio = ""
while opcio != "E":
    print("Monitorització de serveis")
    print("-------------------------")
    print("A. Afegir servei")
    print("B. Mostrar serveis")
    print("C. Eliminar servei")
    print("D. Verificar serveis")
    print("E. Sortir")
    opcio = input("Tria una opció: ").upper()
    if opcio == "A":
       nou_servei = input("Introdueix el nom del servei que vols afegir: ").strip()
       if nou_servei in serveis:
           print("El servei ja esta en la llista no es pot afegir.")
       else:
           serveis.append(nou_servei)
           print(f"El servei {nou_servei} s' afegit correctament a la llista.")
    elif opcio == "B":
        i = 0
        for s in serveis:
            print(f"{i}: {s}")
            i += 1
    elif opcio == "C":
        num = int(input("Introdueix el numero del servei que vols eliminar: "))
        if num < 0 or num >= len(serveis):
            print(f"El numero {num} no es correspon a cap numero en la llista.")
            print("Torna ha seleccionar la opció B per llistar els serveis amb el seu nùmero corresponent a la seva posició.")
        else:
            servei_eliminat = serveis.pop(num)
            print(f"El servei {servei_eliminat} eliminat correctament...")
    elif opcio == "D":
        for x in serveis:
            resultat = subprocess.run(["systemctl", "is-active", "--quiet", x])
            if resultat.returncode == 0:
                print(f"{x}: actiu")
            else:
                print(f"{x}: inactiu")
    else:
        print("Error Torna a introduir una de les opcions vàlides")
print("Sortint del programa")