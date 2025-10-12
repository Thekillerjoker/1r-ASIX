import os
usuari = input("escriu el teu usuari:")
espai = os.popen("sudo du -sh /home/"+ usuari)
print("Espai en disc del directori del usuari")	
print(espai.read())
# correcto