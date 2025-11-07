import os
opcio = input("Escull una ocpió 1 o 2: ").strip()

if opcio == "1":
    fitxer = input("Escriu el nom del fitxer: ").strip()
    if not os.path.exists(fitxer):
        print("Error: Fitxer inexistent")
    else:
        fitxer_sha = fitxer + ".SHA"
        if os.path.exists(fitxer_sha):
            resposta = input("El fitxer .SHA ja existeix. El vols sobrescriure? (S/N): ").strip().upper()
            if resposta == "N":
                print("No s'ha sobrescrigut el fitxer.")
            elif resposta == "S":
                sortida = os.popen(f"sha256sum {fitxer} 2>/dev/null ").read().strip()
                if sortida == "":
                    print("Error calculant el hash")
                else:
                    valor_hash = sortida.split()[0]
                    f = open(fitxer_sha, "w")
                    f.write(valor_hash + "\n")
                    f.close()
                    print("Hash guardat en", fitxer_sha)
            else:
                print("Operació cancelada: Resposta no válida.")
        else:
            sortida = os.popen(f"sha256sum {fitxer} 2>/dev/null ").read().strip()
            if sortida == "":
                print("Error calculant el hash")
            else:
                valor_hash = sortida.split()[0]
                f = open(fitxer_sha, "w")
                f.write(valor_hash + "\n")
                f.close()
                print("Hash guardat en", fitxer_sha)
elif opcio == "2":
    fitxer = input("Escriu el nom del fitxer: ").strip()
    if not os.path.exists(fitxer):
        print("Error: fitxer inexistent")
    else:
        fitxer_sha = fitxer + ".SHA"
        if not os.path.exists(fitxer_sha):
            print("No existeix el fitxer de vericació.")
        else:
            f = open(fitxer_sha,  "r")
            guardat = f.readline().strip()
            f.close()
            sortida = os.popen(f"sha256sum {fitxer} 2>/dev/null ").read().strip()
            if sortida == "":
                print("Error calculant el hash")
            else:
                actual = sortida.split()[0]
                if actual == guardat:
                    print("El fitxer es Ínteger")
                else:
                    print("El fitxer ha sigut modificat")
else:
    print("OpciÓ no válida")
