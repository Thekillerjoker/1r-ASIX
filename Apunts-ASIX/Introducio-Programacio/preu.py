import os
#os.system('ls -l')

stream = os.popen('cd /; ls -l')
sortida = stream.read()
print("sortida-:", sortida)
