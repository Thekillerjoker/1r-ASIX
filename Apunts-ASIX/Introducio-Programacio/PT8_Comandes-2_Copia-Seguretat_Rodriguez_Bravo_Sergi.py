import os
fitxer = input("Escriu el nom del fitxer: ")
data = os.popen('date +%Y-%m-%d ')
llegirdata = data.read().strip()
Copia = f"{fitxer}_{llegirdata}.gz"

if os.system(f"ls {fitxer} 2>/dev/null ") != 0 :
    print("Error: fitxer inexistent")
elif os.system(f"ls {Copia} 2>/dev/null ") == 0 :
    print("Ja existia la copia d'avui")
else:
    os.system(f"gzip -c {fitxer} > {Copia} ")
    print("Còpia creada correctament")
