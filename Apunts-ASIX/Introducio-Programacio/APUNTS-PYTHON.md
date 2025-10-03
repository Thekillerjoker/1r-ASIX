# Para Hacer comandos de shel a python se usa el modulo import os.
*Esto sirve para que tu al ejecutar el codigo en un sistema operativo te cargue solo el codigo que este dentro de la libreria de import os, y asi no tenga que cargar todo el codigo*
```python
import os
os.system('ls -l')

```
## Para hacerlo con guardando a salida:
```python
import os
stream = os.popen('ls -l')
sortida = stream.read()
print("sortida", sortida)
```
