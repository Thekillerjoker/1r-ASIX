import os
opcio = 0
while opcio != 4:
    print("-----------------------------")
    print("Menú D'ADMINISTRACIO")
    print("1. Mostrar usuaris del sistema")
    print("2. Mostrar adreça IP local")
    print("3. Llistar processos actius")
    print("4. Sortir")
    print("-----------------------------")
    opcio = int(input("Escull una opció: "))
    if opcio == 1:
        os.system("cat /etc/passwd ")
    elif opcio == 2:
        os.system("hostname -I ")
    elif opcio == 3:
        os.system("ps -e ")
    elif opcio == 4:
        print("Surtint del programa...")
    else:
        print("Opció no vàlida.  Torna a Intentar-ho.")